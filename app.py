from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    return resp

if __name__ == "__main__":
    app.run()