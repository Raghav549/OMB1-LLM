import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateHybridBrain

brain = OMB1UltimateHybridBrain()

class Gateway(BaseHTTPRequestHandler):
    def _send(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        payload = json.loads(self.rfile.read(content_length).decode('utf-8'))
        
        if self.path == '/api/chat':
            content, dtype = brain.smooth_reply_stream(payload.get("prompt", ""))
            self._send({"reply": content, "type": dtype})
        elif self.path == '/api/train':
            for item in payload.get("dataset", []):
                brain.learn(item['input'], item['data'], item.get('type', 'text'))
            self._send({"status": "Success"})

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    HTTPServer(('', port), Gateway).serve_forever()
