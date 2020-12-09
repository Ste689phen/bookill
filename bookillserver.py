from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv

HOST = 'localhost'
PORT = 8000



class EchoHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = init(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)

        self.write_response(body)

    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)

        print(self.headers)
        print(content.decode('utf-8'))


def main():
    server = HTTPServer((BIND_HOST, PORT), echoHandler)
    print('Echo server now running on ')
    server.serve_forever()
