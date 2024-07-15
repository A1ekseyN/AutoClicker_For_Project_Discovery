from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse.urlparse(self.path).query
        params = urlparse.parse_qs(query)
        code = params.get('code')
        if code:
            print(f'Код авторизации: {code[0]}')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Authorization code received. You can close this window.')
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'No authorization code found.')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
