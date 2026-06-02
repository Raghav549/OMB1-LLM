from omb1_api import OMB1APIGateway
import io

def app(environ, start_response):
    # Gunicorn se request lekar local request object banate hain
    class MockRequest:
        def __init__(self, environ):
            self.environ = environ
            self.rfile = io.BytesIO(environ['wsgi.input'].read())
            self.headers = environ
        def makefile(self, mode, bufsize=0):
            return self.rfile

    # Mock server object jo BaseHTTPRequestHandler ko chahiye
    class MockServer:
        def __init__(self):
            self.server_address = ('', 8080)

    # Gateway ko initialize karte hain
    handler = OMB1APIGateway(MockRequest(environ), ('', 8080), MockServer())
    
    # Response setup
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [b'{"status": "OMB1 Ready"}']

if __name__ == "__main__":
    from http.server import HTTPServer
    httpd = HTTPServer(('', 8080), OMB1APIGateway)
    print("🚀 Local Server Running...")
    httpd.serve_forever()
