# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: API GATEWAY (PERFECT EDITION)
# =====================================================================

import json
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateHybridBrain

# Instance initiated perfectly with correct class name matching wsgi
omb1_instance = OMB1UltimateHybridBrain()

class OMB1APIGateway(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
            
            # ENDPOINT 1: DATA PACK TRAINING STREAMER
            if self.path == '/api/train':
                dataset = payload.get("dataset", [])
                if not dataset:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "No dataset packet found"}).encode('utf-8'))
                    return
                
                omb1_instance.mass_train_pack(dataset)
                self._set_headers(200)
                self.wfile.write(json.dumps({"status": "Success", "message": f"{len(dataset)} records mapped to Pi infinity set successfully."}).encode('utf-8'))
                return

            # ENDPOINT 2: CORE CHAT PROCESSING
            elif self.path == '/api/chat':
                user_prompt = payload.get("prompt", "").strip()
                if not user_prompt:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Empty prompt sequence"}).encode('utf-8'))
                    return
                
                response_payload = omb1_instance.smooth_reply_stream(user_prompt)
                self._set_headers(200)
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))
                return
                
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Resource pathway not found"}).encode('utf-8'))

        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OMB1APIGateway)
    print(f"🚀 [MUKTI LLM CORE GATEWAY LIVE] Server running on port: {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
