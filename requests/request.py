

class Request:
    def __init__(self, file) -> None:
        self.file = file
        self.method = ''
        self.url = ''
        self.protocol = ''
        self.headers = {}
        self.body = None
        self.parse_request_data()
        self.parse_headers()
        self.parse_body()

    def parse_body(self):
        content_length = self.headers.get('Content-Length')
        if content_length:
            self.body = self.file.read(int(content_length))

    def parse_request_data(self):
        request_data = self.read_line()
        self.method, self.url, self.protocol = request_data.split()
        if self.protocol != 'HTTP/1.1':
            raise ValueError

    def parse_headers(self):
        while True:
            header = self.read_line()
            if not header:
                break

            name, value = header.split(': ')
            self.headers[name] = value

    def read_line(self):
        return self.file.readline().decode().strip()

