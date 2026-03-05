import subprocess

class Reviewer:
    def get_repo_context(self, commit_range=None):
        # Grounding: Real tool use to get diffs
        cmd = ["git", "diff", "main...HEAD"] if not commit_range else ["git", "diff", commit_range]
        diff = subprocess.check_output(cmd).decode("utf-8")
        return diff

    def analyze(self, diff):
        # System prompt for Reviewer focusing on categorization and risk
        prompt = f"Analyze this diff. Categorize (feature/bug/refactor), assess risk (low/med/high), and find issues:\n{diff}"
        return ollama_client.generate(prompt)