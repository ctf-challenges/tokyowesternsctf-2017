from flask import Flask, Response, stream_with_context, request

import requests

from sanitizer import urlsanitize
from urlparse import urlparse

app = Flask(__name__)

@app.before_request
def proxy():
    if request.method not in ["GET"]:
        return "{} is not allowed".format(request.method), 405
    url = request.url
    pr = urlparse(url)
    if pr.scheme not in ['http', 'https']:
        return "only HTTP or HTTPS is allowed", 400
    if pr.hostname in ['localhost', '127.0.0.1'] and pr.port == 8080:
        return "recursion detected", 400
    url = urlsanitize(url)
    headers = {k:v for k,v in request.headers if v}
    try:
        req = requests.get(url, headers=headers, stream=True)
    except:
        return "request failed", 500
    headers = dict(req.headers)
    if 'Content-Encoding' in headers: del(headers['Content-Encoding'])
    return Response(stream_with_context(req.iter_content()), headers=headers)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
