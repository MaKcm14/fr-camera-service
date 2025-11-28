import cv2
import time

from . import errors
from cv2.typing import MatLike

# CameraAPI provides the API for the camera's interaction.
class CameraAPI:
    _conn: cv2.VideoCapture

    def __init__(self, camera_idx: int):
        op: str = "repo.camera.capi.CameraAPI.__init__"

        self._conn = cv2.VideoCapture(camera_idx)

        self._conn.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self._conn.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self._conn.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if not self._conn.isOpened():
            raise errors.CameraAPIError(
                f"error of the {op}: error of openning the video-capture conn " \
                f"with the camera №{camera_idx}", 
                errors.CameraAPIErrCodes.ERR_CONN,
            )


    # read_frame defines the logic of reading the frame from the camera.
    def read_frame(self) -> MatLike:
        op: str = "repo.camera.capi.CameraAPI.read_frame"

        for _ in range(5):
            self._conn.grab()

        flag_read_success, frame = self._conn.read()

        if not flag_read_success:
            raise errors.CameraAPIError(
                f"error of the {op}: error of reading the frame",
                errors.CameraAPIErrCodes.ERR_FRAME_READING,
            )

        return frame


    # close defines the logic of releasing the resources of the camera's connection.
    def close(self):
        self._conn.release()
