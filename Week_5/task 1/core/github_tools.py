# core/github_tools.py
import subprocess

class GitHubTools:
    def get_diff(self, base="main", head="HEAD"):
        """Grounding: Get real git diff evidence."""
        try:
            return subprocess.check_output(
                ["git", "diff", f"{base}...{head}"], 
                stderr=subprocess.STDOUT
            ).decode()
        except subprocess.CalledProcessError:
            return "Error: Could not retrieve git diff."

    def read_file(self, filepath):
        """Grounding: Read file content for context."""
        with open(filepath, 'r') as f:
            return f.read()

    def create_on_github(self, title, body, is_pr=False):
        """Tool Use: Final API call (requires human approval first)."""
        # Placeholder for PyGitHub logic
        print(f"[Tool] Successfully created {'Pull Request' if is_pr else 'Issue'}: {title}")