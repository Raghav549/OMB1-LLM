# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: COMPLETED API GATEWAY ROUTER (CHAT + GRAPHICS + TRAINING)
# =====================================================================

import json
import base64
import io
from PIL import Image
from http.server import BaseHTTPRequestHandler, HTTPServer
from omb1_brain import OMB1UltimateHybridBrain

# Initialize single global instance of our upgraded brain
omb1_instance = OMB1UltimateHybridBrain()

# Pre-seeding corporate Identity
omb1_instance.tatkal_grahanam("Mool_Sutra", "सत्यमेव जयते")

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
        """ Unified API Channel for Chat, Vision Parsing and Graphics Stream """
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode('utf-8'))
                user_prompt = payload.get("prompt", "").strip()
                action = payload.get("action", "ask")
                image_base64 = payload.get("image", "") 
                
                # 1. PROCESS INCOMING VISUAL IMAGES (If Any)
                visual_report = None
                if image_base64:
                    try:
                        if "," in image_base64:
                            image_base64 = image_base64.split(",")[1]
                        img_bytes = base64.b64decode(image_base64)
                        pil_img = Image.open(io.BytesIO(img_bytes))
                        
                        # Send image to get processed locally via Pi matrix
                        visual_report = omb1_instance.analyze_visual_data(pil_img)
                    except Exception as visual_err:
                        print(f"⚠️ API Layer Visual Error: {str(visual_err)}")

                if not user_prompt and not image_base64:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Empty prompt received"}).encode('utf-8'))
                    return

                # 2. PASS TO UPGRADED DYNAMIC COGNITION BRAIN
                response_payload = omb1_instance.smooth_reply_stream(user_prompt)
                
                # Append visual analytics logs if available
                if visual_report:
                    response_payload["visual_analysis"] = visual_report
                
                # 3. DISPATCH JSON DATA BACK TO FRONTEND
                self._set_headers(200)
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))
                
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Path endpoint does not exist"}).encode('utf-8'))

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OMB1APIGateway)
    print(f"🚀 [ZERO API GATEWAY OPERATIONAL] Production Target Bound to Port: {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 API Server shut down cleanly.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
