from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv

PORT = 8008


class echoHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)

        self.write_response(body)

    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)

        print(self.headers)
        print(content.decode('utf-8'))


def main():
    server = HTTPServer(('', PORT), echoHTTPRequestHandler)
    print('Echo server now running...')
    server.serve_forever()


if __name__ == '__main__':
    main()
