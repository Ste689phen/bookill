from http.server import HTTPServer, BaseHTTPRequetHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('is this working?' .encode())




def main():
    PORT = 8080
    server = HTTPServer(('ip-172-31-25-240', PORT) echoHandler)
    print('Echo server now running')
    server.serve_forever()


if __name__ = '__main__':
    main()    
