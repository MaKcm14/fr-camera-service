import time
import base64
from flask import Flask, jsonify, send_from_directory
from services.server.interactor import FlowInteractor

class Controller:
    _flow: FlowInteractor
    _read_delay: float

    def __init__(self, flow: FlowInteractor, read_delay: float):
        self._flow = flow
        self._read_delay = read_delay
        self.app = Flask(__name__)
        self.config_endpoints()


    def config_endpoints(self):
        self.app.add_url_rule("/", view_func=self.index)
        self.app.add_url_rule("/img/capybara", view_func=self.get_capybara_img)
        self.app.add_url_rule("/enqueue", view_func=self.handler_get_frame)


    def index(self):
        return send_from_directory('static', 'index.html')


    def get_capybara_img(self):
        return send_from_directory('static', 'capybara.jpg')


    def handler_get_frame(self):
        time.sleep(self._read_delay)

        msg = f"Записываем Вас в очередь..."
        dto, frame = self._flow.notify()

        if frame is not None:
            frame = base64.b64encode(frame).decode('utf-8')
        else:
            return jsonify({"error": "camera API's error"}), 400

        if dto.enqueued:
            msg = f"Вы были записаны"
        else:
            return jsonify({
                "enqueued": dto.enqueued,
                "ticket_id": -1,
                "message": msg
            }), 200

        return jsonify({
            "enqueued": dto.enqueued,
            "ticket_id": dto.ticket_id,
            "image_bytes": frame,
            "message": msg
        }), 200


    def run(self):
        self.app.run(host="169.254.1.1", port=9090)
