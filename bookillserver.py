from http.server import HTTPServer, BaseHTTPRequetHandler

BIND_HOST = 'localhost'
PORT = 8080

class echoHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('is this working?' .encode())




def main():
    server = HTTPServer((BINDHOST, PORT) echoHandler)
    print('Echo server now running')
    server.serve_forever()


if __name__ = '__main__':
    main()
