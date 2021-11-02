from datetime import datetime

def app(environ, start_response):
    data = b"time: "
    data += bytes(str(datetime.now().time()), "utf-8")
    data += b"\nurl: "
    data += bytes(str(environ.get('PATH_INFO', '')), "utf-8")
    data += b"\n"
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])