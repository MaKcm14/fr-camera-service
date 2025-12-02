import time
import requests
from flask import Flask, jsonify, send_from_directory

class Controller:
    _read_delay: float
    _socket: str
    _queue: list

    def __init__(self, read_delay: float, socket: str):
        self._read_delay = read_delay
        self.app = Flask(__name__)
        self._socket = socket
        self._queue = []
        self.config_endpoints()


    def config_endpoints(self):
        self.app.add_url_rule("/", view_func=self.index)
        self.app.add_url_rule("/invite", view_func=self.handler_invite)


    def index(self):
        return send_from_directory('static', 'index.html')


    def handler_invite(self):
        time.sleep(self._read_delay)

        resp = requests.get(f"http://{self._socket}/user/invite")
        if resp.status_code == 200:
            data = resp.json()
        else:
            return jsonify({
            "message": ""
        }), 200

        if len(self._queue) == 0 or self._queue[-1]["ticket_id"] != data['ticket_id']:
            if len(self._queue) == 10:
                self._queue = self._queue[1:]
            self._queue.append({
                "ticket_id": data['ticket_id'],
                "window_id": data['window_id']
            })

        return jsonify({
            "ticket_id": data['ticket_id'],
            "window_id": data['window_id'],
            "queue": self._queue,
            "message": "Information ticket for"
        }), 200


    def run(self):
        self.app.run(host="169.254.1.1", port=9999)
