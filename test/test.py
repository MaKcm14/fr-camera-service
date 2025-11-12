import base64
from flask import Flask, request, jsonify

count = 0
count_frame = 0
app = Flask(__name__)

@app.route("/user/invite", methods=['GET'])
def handler_user_invite():
    global count
    count += 1

    if count % 2:
        return jsonify({"window_id": 10, "ticket_id": 1313}), 200
    
    return jsonify({"window_id": 22, "ticket_id": 9090}), 200


@app.route("/send/frame", methods=['POST'])
def handler_frames():
    global count_frame
    with open(f"data/photo-{count_frame}.png", 'wb') as f:
        f.write(base64.b64decode(request.get_json().get("image_base64")))

    count_frame += 1

    if count_frame % 10 != 0:
        return jsonify({"enqueued": False,
            "error": "couldn't recognize the man"
        }), 200

    return jsonify({"enqueued": True,
        "person_id": 130,
        "ticket_id": 111,
    }), 200


app.run(host='localhost', port=8080)
