from controllers.pages_controller import PagesController, Controller


class Router:
    def __init__(self):
        self.routes = {
            'get': [],
            'post': []
        }

    def add(self, http_method: str, url: str, ctrl: Controller, method: str):
        self.routes[http_method].append(
            {
                'url': url,
                'ctrl': ctrl,
                'method': method
            }
        )

    def get(self, *args):
        self.add('get', *args)

    def post(self, *args):
        self.add('post', *args)

    def run(self, request, response):
        http_method = request.method.lower()
        method_routes = self.routes.get(http_method)

        route = None
        for r in method_routes:
            url = request.url.rsplit('/', 1)[0] or request.url
            if 'css' in url:
                url = '/css'

            if r['url'] == url:
                route = r
                break

        try:
            ctrl = route['ctrl'](request, response)
            getattr(ctrl, route['method'])()

        except Exception:
            PagesController.not_found(request, response)
