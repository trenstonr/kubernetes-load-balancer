import json
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8000"))
HOSTNAME = socket.gethostname()

class Handler(BaseHTTPRequestHandler):
    def _respond(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode() if length else ""
        payload = json.dumps({
            "host": HOSTNAME,
            "method": self.command,
            "path": self.path,
            "body": body,
        }).encode() + b"\n"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    do_GET = do_POST = do_PUT = do_DELETE = _respond


if __name__ == "__main__":
    print(f"Listening on :{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
