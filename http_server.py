import http.server

port = 8035

address = ("",port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"Serveur démarré sur le port {port}")

httpd.serve_forever()