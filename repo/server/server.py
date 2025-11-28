import base64
import enum
import requests

from repo.server.errors import *

class ServerDTO:
    enqueued: bool
    person_id: int
    ticket_id: int

    def __init__(self):
        self.enqueued = False
        self.person_id = -1
        self.ticket_id = -1

    def set_enqueued(self, enqueued: bool):
        self.enqueued = enqueued

    def unmarshal(self, json):
        self.enqueued = bool(json["enqueued"])
        self.person_id = int(json["person_id"])
        self.ticket_id = int(json["ticket_id"])
        return self

# Endpoints defines the enum that describes the server's endpoints.
class Endpoints(enum.Enum):
    POST_FRAME: str = "/send/frame"


# APIServer defines the logic of interaction with the server-API.
class APIServer:
    _socket: str

    def __init__(self, socket: str):
        self._socket = socket


    def send_frame(self, frame: bytes) -> ServerDTO:
        resp = requests.post(f'http://{self._socket}{Endpoints.POST_FRAME.value}', 
            json={"image_base64": base64.b64encode(frame)},
        )

        data = resp.json()

        if "error" in data and len(str(data["error"])) != 0:
            raise ServerErr(str(data["error"]), ServerErrorCodes.ERR_POST_REQUEST.value)
        elif resp.status_code >= 500:
            raise ServerErr("error of the server's handlers", 
                        ServerErrorCodes.ERR_SERVER_HANDLER.value)

        if resp.status_code < 300:
            return ServerDTO().unmarshal(data)

        dto = ServerDTO()
        dto.set_enqueued(False)
        return dto
