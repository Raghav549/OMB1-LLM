import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateHybridBrain

# Instance initiate kiya
omb1_instance = OMB1UltimateHybridBrain()

# Gunicorn ke liye 'app' variable export kar rahe hain
app = omb1_instance 

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
            content, dtype = omb1_instance.query_brain(payload.get("prompt", ""))
            self._send({"reply": content, "type": dtype})
            
        elif self.path == '/api/train':
            for item in payload.get("dataset", []):
                omb1_instance.learn(item['input'], item['data'], item.get('type', 'text'))
            self._send({"status": "Success"})

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    HTTPServer(('', 8080), Gateway).serve_forever()
