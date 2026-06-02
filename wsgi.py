# wsgi.py
import json
from omb1_api import omb1_instance

def app(environ, start_response):
    # 1. CORS Preflight (OPTIONS) request ko handle karna
    if environ['REQUEST_METHOD'] == 'OPTIONS':
        status = '200 OK'
        response_body = b''
        response_headers = [
            ('Content-Type', 'application/json'),
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'POST, OPTIONS, GET'),
            ('Access-Control-Allow-Headers', 'Content-Type, Authorization, Accept'),
            ('Content-Length', '0')
        ]
        start_response(status, response_headers)
        return [response_body]

    # 2. Asli POST request ko handle karna
    elif environ['REQUEST_METHOD'] == 'POST':
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            request_body = environ['wsgi.input'].read(request_body_size)
            payload = json.loads(request_body)
            
            # OMB1 Engine call
            user_prompt = payload.get("prompt", "")
            action = payload.get("action", "ask")
            
            # Logic Routing
            if "draw" in user_prompt.lower() or "design" in user_prompt.lower() or action == "visual":
                response_data = {"type": "Visual_Art", "data": omb1_instance.generate_art_loop(user_prompt)}
            else:
                response_data = omb1_instance.smooth_reply_stream(user_prompt)
            
            status = '200 OK'
            response_body = json.dumps(response_data, ensure_ascii=False).encode('utf-8')
        except Exception as e:
            status = '500 Internal Server Error'
            response_body = json.dumps({"error": str(e)}).encode('utf-8')
    else:
        status = '405 Method Not Allowed'
        response_body = b'{"error": "Only POST allowed"}'

    # POST ya baaki methods ke response mein bhi CORS headers jorna zaroori hai
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body))),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'POST, OPTIONS, GET'),
        ('Access-Control-Allow-Headers', 'Content-Type, Authorization, Accept')
    ]
    
    start_response(status, response_headers)
    return [response_body]
