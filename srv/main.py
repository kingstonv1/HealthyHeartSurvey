from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello!", "utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers = self.headers,
            environ = {"REQUEST_METHOD": "POST"}
        )


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")