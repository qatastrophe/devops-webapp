from http.server import HTTPServer, BaseHTTPRequestHandler


PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
