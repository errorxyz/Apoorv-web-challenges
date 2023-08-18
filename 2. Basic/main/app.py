from flask import Flask, render_template, request
import subprocess
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/exec", methods=["POST"])
def exec():
    command = request.json['command']
    return subprocess.getoutput(command)

if __name__ == '__main__':
    http_server = WSGIServer(('127.1', 5001), app)
    http_server.serve_forever()