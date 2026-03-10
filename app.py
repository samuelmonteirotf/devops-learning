import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def soma(a, b):
    """Retorna a soma de dois valores."""
    return a + b


def subtrai(a, b):
    """Retorna a subtração do primeiro valor pelo segundo."""
    return a - b


def multiplica(a, b):
    """Retorna a multiplicação de dois valores."""
    return a * b


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            response = json.dumps({
                "status": "ok",
                "message": "DevOps Learning Project is running in Docker!"
            })
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def run(host="0.0.0.0", port=8000):
    server = HTTPServer((host, port), AppHandler)
    print(f"Server running at http://{host}:{port}/")
    server.serve_forever()


if __name__ == "__main__":
    run()
