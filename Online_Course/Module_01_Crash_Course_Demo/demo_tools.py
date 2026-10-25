"""Module 1 permits agent writes only to its implementation file."""
from pathlib import Path
import sys

COURSE = Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path:
    sys.path.insert(0, str(COURSE))
from shared.repo_tools import RepoTools


class DemoTools(RepoTools):
    def write_file(self, path, content):
        target = self._path(path)
        if target != self._path('src/checkout.py'):
            raise PermissionError('Only src/checkout.py may be edited in Module 1.')
        return super().write_file(path, content)
