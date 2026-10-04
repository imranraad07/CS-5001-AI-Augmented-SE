"""Allowlisted repository tools with a workspace boundary."""
from __future__ import annotations
from pathlib import Path
import subprocess, json

class RepoTools:
    def __init__(self,root): self.root=Path(root).resolve(); self.audit=[]
    def _path(self,p):
        x=(self.root/p).resolve()
        if x!=self.root and self.root not in x.parents: raise PermissionError("path escapes workspace")
        return x
    def read_file(self,path):
        p=self._path(path); self.audit.append({"tool":"read_file","path":path}); return p.read_text()
    def write_file(self,path,content):
        p=self._path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content); self.audit.append({"tool":"write_file","path":path}); return f"wrote {path}"
    def search_repo(self,query):
        hits=[]
        for p in self.root.rglob("*"):
            if p.is_file() and ".git" not in p.parts:
                try:
                    if query.lower() in p.read_text(errors="ignore").lower(): hits.append(str(p.relative_to(self.root)))
                except Exception: pass
        self.audit.append({"tool":"search_repo","query":query}); return hits[:20]
    def run_tests(self):
        cp=subprocess.run(["python","-m","pytest","-q"],cwd=self.root,text=True,capture_output=True,timeout=60)
        out=(cp.stdout+"\n"+cp.stderr).strip(); self.audit.append({"tool":"run_tests","returncode":cp.returncode}); return {"returncode":cp.returncode,"output":out}
    def schemas(self):
        return [
          {"type":"function","function":{"name":"read_file","description":"Read a UTF-8 file inside the demo repository.","parameters":{"type":"object","properties":{"path":{"type":"string"}},"required":["path"]}}},
          {"type":"function","function":{"name":"write_file","description":"Replace a UTF-8 file inside the demo repository. Do not edit tests unless explicitly requested.","parameters":{"type":"object","properties":{"path":{"type":"string"},"content":{"type":"string"}},"required":["path","content"]}}},
          {"type":"function","function":{"name":"search_repo","description":"Search text in repository files.","parameters":{"type":"object","properties":{"query":{"type":"string"}},"required":["query"]}}},
          {"type":"function","function":{"name":"run_tests","description":"Run the real pytest suite in the demo repository.","parameters":{"type":"object","properties":{}}}},
        ]
    def call(self,name,args):
        if name=="read_file": return self.read_file(**args)
        if name=="write_file": return self.write_file(**args)
        if name=="search_repo": return self.search_repo(**args)
        if name=="run_tests": return self.run_tests()
        raise KeyError(name)
