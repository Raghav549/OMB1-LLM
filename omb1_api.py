# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: COMPACT CORE API GATEWAY FOR DEPLOYMENT (RENDER / VERCEL)
# COST: ZERO (Native JSON stream handling, no external heavy libraries)
# =====================================================================

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateBrain

# Active runtime layer setup
omb1_instance = OMB1UltimateBrain()

# Base template seeding at startup
omb1_instance.tatkal_grahanam("Mool_Sutra", "सत्यमेव जयते नानृतं सत्येन पन्था विततो देवयानः।")

class OMB1APIGateway(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        # CORS enabled for future frontends
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_POST(self):
        """ Real-time chat & learning API router """
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode('utf-8'))
                user_prompt = payload.get("prompt", "")
                action = payload.get("action", "ask")  # 'ask' or 'train'
                source = payload.get("source", "User_Live_Feed")
                
                if not user_prompt:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Prompt data cannot be empty"}).encode('utf-8'))
                    return
                
                # Dynamic routing based on request actions
                if action == "train":
                    ptr = omb1_instance.tatkal_grahanam(source, user_prompt)
                    response_payload = {
                        "status": "Success",
                        "pointer": ptr,
                        "message": "Data instantly caught and mapped."
                    }
                else:
                    # Execute instant reasoning stream
                    response_payload = omb1_instance.smooth_reply_stream(user_prompt)
                
                self._set_headers(200)
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))
                
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Route not matched"}).encode('utf-8'))

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OMB1APIGateway)
    print(f"🚀 [ZERO API GATEWAY LIVE] Bound to production port: {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server pipeline stopped safely.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
