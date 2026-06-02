# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: FULL INTEGRATED API GATEWAY (CHAT + VISUAL ENGINE)
# =====================================================================

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateHybridBrain

# Active runtime layer setup
omb1_instance = OMB1UltimateHybridBrain()

# Base template seeding
omb1_instance.tatkal_grahanam("Mool_Sutra", "सत्यमेव जयते नानृतं सत्येन पन्था विततो देवयानः।")

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
        """ Integrated API Router: Handles Chat, Training, and Visual Art Generation """
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode('utf-8'))
                user_prompt = payload.get("prompt", "")
                action = payload.get("action", "ask")
                source = payload.get("source", "User_Live_Feed")
                
                if not user_prompt:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Prompt data empty"}).encode('utf-8'))
                    return
                
                # --- INTELLIGENT ROUTING LOGIC ---
                # Check for Visual Art/Design command
                if "draw" in user_prompt.lower() or "design" in user_prompt.lower() or action == "visual":
                    # Visual Engine se art generate karein
                    art_result = omb1_instance.generate_art_loop(user_prompt)
                    response_payload = {
                        "type": "Visual_Art_Generation",
                        "data": art_result,
                        "message": "Mathematical Engine Render Complete."
                    }
                elif action == "train":
                    ptr = omb1_instance.tatkal_grahanam(source, user_prompt)
                    response_payload = {"status": "Success", "pointer": ptr, "message": "Knowledge mapped."}
                else:
                    # Normal Intelligent Chat
                    response_payload = omb1_instance.smooth_reply_stream(user_prompt)
                
                self._set_headers(200)
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))
                
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Route not found"}).encode('utf-8'))

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OMB1APIGateway)
    print(f"🚀 [ZERO API GATEWAY LIVE] Bound to production port: {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped safely.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
