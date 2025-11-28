import random
import base64
from flask import Flask, request, jsonify

count_frame = 0
app = Flask(__name__)

@app.route("/test", methods=['GET'])
def handler_test_request():
    return {
        "status": "ok",
        "message": "connection is stable"
    }

@app.route("/user/invite", methods=['GET'])
def handler_user_invite():
    return jsonify({
            "window_id": random.randint(1, 100), 
            "ticket_id": random.randint(1, 1000)
    }), 200


@app.route("/send/frame", methods=['POST'])
def handler_frames():
    global count_frame
    with open(f"../data/photo-{count_frame}.png", 'wb') as f:
        f.write(base64.b64decode(request.get_json().get("image_base64")))

    if random.randint(0, 1) == 0:
        return jsonify({"enqueued": False,
            "error": "couldn't recognize the man"
        }), 200

    return jsonify({"enqueued": True,
        "person_id": random.randint(1, 100),
        "ticket_id": random.randint(1, 1000),
    }), 200


app.run(host='0.0.0.0', port=8080)
