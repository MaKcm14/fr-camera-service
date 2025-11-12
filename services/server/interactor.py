from logging import Logger

from repo.server.server import APIServer, ServerDTO
from repo.server.errors import ServerErr
from services.camera.interactor import CameraInteractor
from services.converter import Formats

# FlowInteractor defines the logic of the frame processing
# and control the frame flow to the server.
class FlowInteractor:
    _api: APIServer
    _camera: CameraInteractor
    _server_socket: str
    _logger: Logger

    def __init__(self, camera: CameraInteractor, api: APIServer, log: Logger):
        self._camera = camera
        self._api = api
        self._logger = log


    # get_frame_png defines the logic of getting the byte frame's view in the .png.
    def _get_frame_png(self) -> bytes | None:
        return self._camera.get_frame(Formats.PNG_FORMAT)

    # notify defines the logic of notifying the server about getting a new data.
    def notify(self) -> tuple[ServerDTO, bytes]:
        frame = self._get_frame_png()
        if frame is None:
            dto = ServerDTO()
            dto.set_enqueued(False)
            return dto, None

        try:
            return self._api.send_frame(frame), frame
        except ServerErr as s:
            self._logger.error(f"errors of the server.notify: {s.get_message()}")
            dto = ServerDTO()
            dto.set_enqueued(False)
            return dto, frame


    # close defines the logic of releasing the resources of the object.
    def close(self):
        self._camera.close()
