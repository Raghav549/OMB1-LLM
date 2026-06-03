# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: FINAL API GATEWAY - NO HACKS, NO FAILURES
# =====================================================================

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateHybridBrain

# Initializing brain instance
omb1_instance = OMB1UltimateHybridBrain()

class OMB1APIGateway(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
            
            # TRAINING ENDPOINT
            if self.path == '/api/train':
                dataset = payload.get("dataset", [])
                if not isinstance(dataset, list):
                    return self._send_response(400, {"status": "Error", "msg": "Invalid format"})
                
                omb1_instance.mass_train_pack(dataset)
                return self._send_response(200, {"status": "Success", "message": "Data saved to Pi-Grid"})

            # CHAT ENDPOINT
            elif self.path == '/api/chat':
                prompt = payload.get("prompt", "")
                reply = omb1_instance.smooth_reply_stream(prompt)
                return self._send_response(200, reply)
            
            else:
                return self._send_response(404, {"status": "Error", "msg": "Path not found"})

        except Exception as e:
            return self._send_response(500, {"status": "Error", "msg": str(e)})

# SERVER START LOGIC
if __name__ == "__main__":
    port = 8080
    httpd = HTTPServer(('', port), OMB1APIGateway)
    print(f"🚀 [MUKTI LLM GATEWAY] Running on {port}")
    httpd.serve_forever()
