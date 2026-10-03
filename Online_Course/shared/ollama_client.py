"""Small dependency-free client for a local Ollama server."""
from __future__ import annotations
import json, urllib.request, urllib.error

class OllamaError(RuntimeError): pass

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="qwen3:4b", embedding_model="embeddinggemma"):
        self.base_url=base_url.rstrip("/"); self.model=model; self.embedding_model=embedding_model

    def _post(self,path,payload):
        req=urllib.request.Request(self.base_url+path,data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"})
        try:
            with urllib.request.urlopen(req,timeout=180) as r: return json.loads(r.read().decode())
        except (urllib.error.URLError,TimeoutError) as e:
            raise OllamaError(f"Cannot reach Ollama at {self.base_url}. Start Ollama and pull the configured model. {e}") from e

    def chat(self,messages,tools=None,model=None):
        body={"model":model or self.model,"messages":messages,"stream":False}
        if tools: body["tools"]=tools
        return self._post("/api/chat",body)["message"]

    def generate(self,prompt,system=""):
        msgs=[]
        if system: msgs.append({"role":"system","content":system})
        msgs.append({"role":"user","content":prompt})
        return self.chat(msgs).get("content","")

    def embed(self,texts):
        if isinstance(texts,str): texts=[texts]
        return self._post("/api/embed",{"model":self.embedding_model,"input":texts})["embeddings"]

    def models(self):
        try:
            with urllib.request.urlopen(self.base_url+"/api/tags",timeout=5) as r: return [m["name"] for m in json.loads(r.read().decode()).get("models",[])]
        except Exception: return []
