import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body.decode())

with socketserver.TCPServer(("", 8000), MyHandler) as httpd:
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
