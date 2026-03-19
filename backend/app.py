import json
import time

from http.server import HTTPServer, BaseHTTPRequestHandler


PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            health_status = {
                "status": "healthy",
                "timestamp": time.time(),
            }

            self.wfile.write(json.dumps(health_status).encode())
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
