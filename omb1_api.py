# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: FULL INTEGRATED API GATEWAY (CHAT + VISUAL ENGINE)
# =====================================================================

import json
import base64
import io
from PIL import Image
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
        """ Integrated API Router: Handles Chat, Training, and Visual Analysis """
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode('utf-8'))
                user_prompt = payload.get("prompt", "")
                action = payload.get("action", "ask")
                source = payload.get("source", "User_Live_Feed")
                
                # Frontend se aane waala image data (Base64 format mein)
                image_data = payload.get("image", "") 
                
                # 1. AUTONOMOUS VISUAL CATCH LAYER
                visual_analysis = None
                if image_data:
                    try:
                        # Agar base64 ke sath 'data:image/jpeg;base64,' jaisa header ho toh use clean karein
                        if "," in image_data:
                            image_data = image_data.split(",")[1]
                        
                        # Pure python se binary bytes mein convert karke image object banayein
                        img_bytes = base64.b64decode(image_data)
                        pil_img = Image.open(io.BytesIO(img_bytes))
                        
                        # Brain ke local pixel-analysis engine ko train hone ke liye bhejeb
                        visual_analysis = omb1_instance.analyze_visual_data(pil_img)
                        print(f"📸 API Gateway intercepted image data. Analysis: {visual_analysis['status']}")
                    except Exception as img_err:
                        print(f"⚠️ Visual Stream Error: {str(img_err)}")

                if not user_prompt and not image_data:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Prompt and Image data both empty"}).encode('utf-8'))
                    return
                
                # 2. INTELLIGENT ROUTING LOGIC
                # Check for Visual Art Generation command (User text se draw karne ko bole)
                if "draw" in user_prompt.lower() or "design" in user_prompt.lower() or action == "visual":
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
                    # Normal Autonomous Chat Logic
                    response_payload = omb1_instance.smooth_reply_stream(user_prompt)
                    
                    # Agar saath mein image parakh engine chala hai, toh report inject karein
                    if visual_analysis:
                        response_payload["visual_analysis"] = visual_analysis
                
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
