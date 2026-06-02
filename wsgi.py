from omb1_api import OMB1APIGateway

# WSGI standard application object (Gunicorn ke liye)
def app(environ, start_response):
    # Yeh Gunicorn ki requests ko handle karega aur 
    # API Gateway ko response pass karega
    gateway = OMB1APIGateway(environ, start_response)
    # Gunicorn expects an iterable, usually the response content
    return [b"OK"]

# Local testing aur startup script ke liye
if __name__ == "__main__":
    from http.server import HTTPServer
    port = 8080
    httpd = HTTPServer(('', port), OMB1APIGateway)
    print(f"🚀 [ZERO API GATEWAY LIVE] Bound to port: {port}")
    httpd.serve_forever()
