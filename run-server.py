from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import mimetypes

root_directory = os.path.dirname(os.path.abspath(__file__)) # абсолютный путь к корню проекта

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            filepath = root_directory + '/index.html'
        else:
            filepath= root_directory + self.path
        self.send_response(200)
        mimetype = mimetypes.guess_type(filepath)
        self.send_header('Content-type', mimetype[0])
        self.end_headers()
        requested_file = open(filepath, 'rb').read()
        self.wfile.write(requested_file)

def run(port = 7842):
    try:
        print(f"Local server was started at http://localhost:{port}/")
        server_address = ('', port)
        my_server = HTTPServer(server_address, RequestHandler)
        os.system(f"start http://localhost:{port}/")
        my_server.serve_forever()
        

    except KeyboardInterrupt:
	    print ('^C received, shutting down the web server')
	    my_server.socket.close()
	

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        run()
    else:
        run(int(sys.argv[1]))
        