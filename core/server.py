from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn


from requests.request import Request
from requests.response import Response
from routers.urls import router


class MyTCPHandler(StreamRequestHandler):
    def handle(self) -> None:
        request = Request(self.rfile)
        response = Response(self.wfile)
        response.add_header('Connetion', 'close')
        router.run(request, response)
        response.send()


class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    ...
