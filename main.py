from socketserver import TCPServer
from core.server import MyTCPHandler, ThreadingTCPServer


HOST = 'localhost', 8000
TCPServer.allow_reuse_address = True
print('Server is started! Link: http://localhost:8000')
with ThreadingTCPServer(HOST, MyTCPHandler) as server:
    server.serve_forever()
