import socket
from time import sleep

from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@sock.route('/')
def handle_ws(ws):
    server_ip = socket.gethostbyname(socket.gethostname())
    while True:
        ws.send(f'Hello from {server_ip}!')
        sleep(5)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
