import http.server
import socketserver

if __name__ == "__main__":
    with socketserver.TCPServer(
        ("", 8080), http.server.SimpleHTTPRequestHandler
    ) as httpd:
        print("Serving on port 80")
        httpd.serve_forever()
