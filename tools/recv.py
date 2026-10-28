"""Tiny local receiver: POST /<name> body -> incoming/figma/<name>. CORS open, localhost only."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
OUT = Path(__file__).resolve().parents[2] / 'incoming' / 'figma'; OUT.mkdir(parents=True, exist_ok=True)
class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*'); self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
    def do_OPTIONS(self): self.send_response(204); self._cors(); self.end_headers()
    def do_POST(self):
        n = Path(self.path).name or 'dump.bin'
        (OUT / n).write_bytes(self.rfile.read(int(self.headers['Content-Length'])))
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b'ok')
HTTPServer(('127.0.0.1', 8799), H).serve_forever()
