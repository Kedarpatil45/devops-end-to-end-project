from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request received!")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello! DevOps project is working.")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)

print("Server running on port 8000")

server.serve_forever()