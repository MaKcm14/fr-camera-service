from services.camera.interactor import CameraInteractor
from services.converter import Formats

# FlowInteractor defines the logic of the frame processing
# and control the frame flow to the server.
class FlowInteractor:
    _camera: CameraInteractor
    _server_socket: str

    def __init__(self, camera: CameraInteractor, server_socket: str):
        self._camera = camera
        self._server_socket = server_socket


    # get_frame_png defines the logic of getting the byte frame's view in the .png.
    def get_frame_png(self) -> bytes | None:
        return self._camera.get_frame(Formats.PNG_FORMAT)


    # close defines the logic of releasing the resources of the object.
    def close(self):
        self._camera.close()
