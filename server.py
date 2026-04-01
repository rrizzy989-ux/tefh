#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse

PORT = 6969

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Remove leading slash
        if path.startswith('/'):
            path = path[1:]
        
        # Remove trailing slash
        if path.endswith('/'):
            path = path[:-1]
        
        # Map clean URLs to actual files (pathname to filename)
        url_map = {
            'pets': 'values_pets.html',
            'eggs': 'values_eggs.html',
            'petwear': 'values_petwear.html',
            'strollers': 'values_strollers.html',
            'food': 'values_food.html',
            'vehicles': 'values_vehicles.html',
            'toys': 'values_toys.html',
            'gifts': 'values_gifts.html',
            'stickers': 'values_stickers.html',
            'houses': 'values_houses.html',
            'values': 'values.html',
            'trades': 'trades.html',
            'calculator': 'calculator.html',
            'blog': 'blog.html',
            'credits': 'credits.html',
            'servers': 'servers.html',
            'value-updates': 'value-updates.html',
            '': 'index.html',
        }
        
        # Check if path matches any mapping
        file_path = None
        if path in url_map:
            file_path = url_map[path]
        elif not path.endswith('.html') and os.path.exists(path + '.html'):
            file_path = path + '.html'
        else:
            file_path = path
        
        # Serve the file directly without redirects
        if file_path and os.path.exists(file_path):
            self.send_response(200)
            if file_path.endswith('.html'):
                self.send_header('Content-type', 'text/html')
            elif file_path.endswith('.css'):
                self.send_header('Content-type', 'text/css')
            elif file_path.endswith('.js'):
                self.send_header('Content-type', 'application/javascript')
            else:
                self.send_header('Content-type', 'application/octet-stream')
            
            with open(file_path, 'rb') as f:
                content = f.read()
            self.send_header('Content-length', len(content))
            self.end_headers()
            self.wfile.write(content)
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running on http://localhost:{PORT}/")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")
