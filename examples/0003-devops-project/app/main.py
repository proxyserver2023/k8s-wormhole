import os.path
from time import sleep
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST='0.0.0.0'
PORT=80
PATH='/var/www/html/index.html'

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()


        if os.path.isfile(PATH):
            with open(PATH, 'r') as f:
                self.wfile.write(bytes(f.read(), 'utf-8'))
        else:
          self.wfile.write(b'Hello, world!')

def run(host, port, server_class=HTTPServer, handler_class=Handler):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      pass
    httpd.server_close()

if __name__ == '__main__':
    print('Starting server...')
    run(HOST, PORT)
