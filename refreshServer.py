import time
import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

PORT = 8001

class RefreshServer(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/refreshMonitor':
            return SimpleHTTPRequestHandler.do_GET(self)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        mtime = os.path.getmtime('.')
        while True:
            if mtime < os.path.getmtime('.'):
                mtime = os.path.getmtime('.')
                self.wfile.write('Changed')
                break 
            time.sleep(1) 

if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', PORT), RefreshServer)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    httpd.server_close()
