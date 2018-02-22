
from tornado import ioloop, httpclient


def get_url():
    for i in range(20000000):
        yield 'https://wrc.edu.np'


i = 0


def handle_request(response):
    print(response.code)
    global i
    i -= 1
    if i == 0:
        ioloop.IOLoop.instance().stop()


http_client = httpclient.AsyncHTTPClient()
for url in get_url():
    i += 1
    print(i, '\n')
    http_client.fetch(url, handle_request, method='HEAD')
ioloop.IOLoop.instance().start()
