# core/agents.py
import re

# ── keyword signals used for evidence-based categorisation ──────────────────
_CATEGORY_SIGNALS = {
    "bugfix":   [r"\bfix(es|ed)?\b", r"\bbug\b", r"\bpatch\b", r"\bhotfix\b",
                 r"\bcrash\b", r"\berror\b", r"\bregression\b"],
    "feature":  [r"\bfeat(ure)?\b", r"\badd(ed|ing)?\b", r"\bnew\b",
                 r"\bimplement(ed|ing)?\b", r"\bintroduce[sd]?\b"],
    "refactor": [r"\brefactor\b", r"\bclean(up)?\b", r"\breach(itect)?\b",
                 r"\bmove[sd]?\b", r"\brename[sd]?\b", r"\brestructure\b"],
    "test":     [r"\btest(s|ing|ed)?\b", r"\bspec\b", r"\bassert\b",
                 r"\bmock\b", r"\bfixture\b"],
    "chore":    [r"\bdep(endency|endencies)?\b", r"\bupgrade\b",
                 r"\bbump\b", r"\bconfig\b", r"\bci\b", r"\bdocs?\b"],
}

_HIGH_RISK_PATTERNS   = [r"\bauth\b", r"\btoken\b", r"\bpassword\b", r"\bsecret\b",
                          r"\bdeploy\b", r"\bdatabase\b", r"\bmigrat\b", r"\bdelete\b",
                          r"\bdrop\b", r"\btruncate\b"]
_MEDIUM_RISK_PATTERNS = [r"\bapi\b", r"\bgateway\b", r"\bserver\b", r"\broute\b",
                          r"\bhandler\b", r"\bmodel\b", r"\bschema\b"]


def _count_lines(diff: str):
    added   = sum(1 for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in diff.splitlines() if l.startswith("-") and not l.startswith("---"))
    return added, removed

def _files_changed(diff: str):
    return re.findall(r"^diff --git a/(.+?) b/", diff, re.MULTILINE)

def _match_signals(text: str, patterns: list) -> bool:
    text_lower = text.lower()
    return any(re.search(p, text_lower) for p in patterns)

def _categorize(diff: str) -> str:
    scores = {cat: 0 for cat in _CATEGORY_SIGNALS}
    for cat, patterns in _CATEGORY_SIGNALS.items():
        for p in patterns:
            if re.search(p, diff, re.IGNORECASE):
                scores[cat] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "unknown"

def _assess_risk(diff: str, added: int, removed: int) -> str:
    if _match_signals(diff, _HIGH_RISK_PATTERNS) or (added + removed) > 200:
        return "high"
    if _match_signals(diff, _MEDIUM_RISK_PATTERNS) or (added + removed) > 50:
        return "medium"
    return "low"


class Reviewer:
    def analyze(self, diff: str) -> dict:
        """
        Grounding: Parse the real git diff to produce an evidence-based review.
        Returns a structured dict with category, risk, files, and issues found.
        """
        print("[Reviewer] Analyzing code changes...")

        if not diff or diff.startswith("Error"):
            return {
                "category": "unknown", "risk": "low",
                "added": 0, "removed": 0, "files": [],
                "summary": "No diff available — nothing to review.",
                "issues": []
            }

        added, removed   = _count_lines(diff)
        files            = _files_changed(diff)
        category         = _categorize(diff)
        risk             = _assess_risk(diff, added, removed)

        # Collect evidence snippets (first 3 changed hunks)
        hunks = re.findall(r"@@[^\n]*\n(?:[^\n]*\n){0,5}", diff)[:3]
        evidence_snippets = [h.strip() for h in hunks]

        # Simple issue detection
        issues = []
        if re.search(r"\bexcept\s*:", diff):
            issues.append("Bare `except:` clause detected — catches all exceptions silently.")
        if re.search(r"\bprint\s*\(", diff) and category != "test":
            issues.append("Debug `print()` statement found in non-test code.")
        if re.search(r"\bTODO\b|\bFIXME\b|\bHACK\b", diff, re.IGNORECASE):
            issues.append("TODO/FIXME/HACK comment left in diff.")
        if removed > added * 2:
            issues.append("Large net deletion — verify nothing critical was removed.")

        summary = (
            f"Categorized as **{category}** | Risk: **{risk}** | "
            f"+{added}/−{removed} lines across {len(files)} file(s)."
        )
        print(f"  → Category : {category}")
        print(f"  → Risk     : {risk}")
        print(f"  → Changes  : +{added}/−{removed} lines in {len(files)} file(s)")
        if issues:
            print(f"  → Issues   : {'; '.join(issues)}")

        return {
            "category": category, "risk": risk,
            "added": added, "removed": removed,
            "files": files, "summary": summary,
            "issues": issues, "evidence": evidence_snippets
        }


class Planner:
    def decide(self, review: dict) -> dict:
        """
        Planning Pattern: Use review evidence to decide the next action.
        All decisions must be justified by the review data.
        """
        print("[Planner] Deciding next steps...")

        category = review.get("category", "unknown")
        risk     = review.get("risk", "low")
        issues   = review.get("issues", [])
        files    = review.get("files", [])

        # Decision logic with evidence-backed justification
        if not files:
            action     = "no_action"
            justification = "Diff is empty — no changes to act on."
        elif risk == "high":
            action        = "create_issue"
            justification = (
                f"High-risk {category} change in {len(files)} file(s). "
                "An issue should gate further review before merging."
            )
        elif category in ("bugfix", "feature") and risk in ("medium", "high"):
            action        = "create_pr"
            justification = (
                f"A {category} of {risk} risk warrants a pull request "
                "so changes can be peer-reviewed before landing."
            )
        elif issues:
            action        = "create_issue"
            justification = (
                f"Code quality issues detected: {'; '.join(issues[:2])}. "
                "An issue tracks these for follow-up."
            )
        elif category in ("refactor", "chore", "test"):
            action        = "create_issue"
            justification = (
                f"A {category} change with {risk} risk. "
                "An issue documents intent and tracks completion."
            )
        else:
            action        = "create_issue"
            justification = (
                f"{category.capitalize()} change detected. "
                "Creating an issue to document and track the change."
            )

        print(f"  → Decision : {action}  ({justification[:80]}...)" if len(justification) > 80
              else f"  → Decision : {action}  ({justification})")

        return {"action": action, "justification": justification, "review": review}


class Writer:
    def draft(self, plan: dict, diff: str) -> dict:
        """
        Drafts the GitHub Issue / PR with Title, Body, Evidence, and Test Plan.
        Everything in the body must be traceable to the diff or the review.
        """
        print("[Writer] Drafting content...")

        review        = plan.get("review", {})
        action        = plan.get("action", "create_issue")
        justification = plan.get("justification", "")
        category      = review.get("category", "unknown")
        risk          = review.get("risk", "low")
        files         = review.get("files", [])
        issues        = review.get("issues", [])
        evidence      = review.get("evidence", [])

        file_list = "\n".join(f"  - `{f}`" for f in files) or "  - (no files detected)"
        issue_list = "\n".join(f"  - {i}" for i in issues) or "  - None detected"

        evidence_block = ""
        if evidence:
            snippet = evidence[0][:300]
            evidence_block = f"\n### Evidence from diff\n```diff\n{snippet}\n```\n"

        # Emoji badges for readability
        category_badge = {"bugfix":"🐛","feature":"✨","refactor":"♻️",
                          "test":"🧪","chore":"🔧"}.get(category, "📝")
        risk_emoji     = {"low":"🟢","medium":"🟡","high":"🔴"}.get(risk, "⚪")

        title = f"{category_badge} [{category.upper()}] Changes in {files[0].split('/')[-1] if files else 'codebase'}"

        body = f"""\
## Summary
{justification}

## Classification
| Field | Value |
|---|---|
| **Category** | {category_badge} {category} |
| **Risk Level** | {risk_emoji} {risk} |
| **Action** | {action.replace('_', ' ').title()} |
| **Lines Changed** | +{review.get('added',0)} / −{review.get('removed',0)} |

## Files Changed
{file_list}
{evidence_block}
## Issues Found
{issue_list}

## Test Plan
- [ ] Run existing test suite and confirm no regressions.
- [ ] Manually verify the changed files behave as expected.
{"- [ ] High-risk change: request a second reviewer." if risk == "high" else ""}

## Notes
> This draft was generated by the GitHub Agent pipeline and reflects only what is present in the diff.
"""
        return {"title": title, "body": body, "action": action}


class Gatekeeper:
    def reflect(self, draft: dict, diff: str) -> str:
        """
        Reflection Pattern: Audit the draft for hallucinations.
        Checks that every file mentioned in the draft actually appears in the diff.
        """
        print("[Gatekeeper] Reflection Pattern: Checking for hallucinations...")

        body  = draft.get("body", "")
        title = draft.get("title", "")

        # 1. Extract backtick-quoted filenames from the draft body
        mentioned_files = re.findall(r"`([^`]+\.[a-z]+)`", body)

        hallucinations = []
        for fname in mentioned_files:
            # Check the base filename appears somewhere in the diff
            if fname not in diff and fname.split("/")[-1] not in diff:
                hallucinations.append(fname)

        # 2. Ensure a test plan is present
        if "Test Plan" not in body:
            return "FAIL - Draft is missing a Test Plan section."

        # 3. Report hallucinations
        if hallucinations:
            return f"FAIL - Draft mentions file(s) not found in diff: {', '.join(hallucinations)}"

        return "PASS"