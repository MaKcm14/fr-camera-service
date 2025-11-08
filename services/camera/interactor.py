from repo.camera.capi import CameraAPI
from services.converter import Formats, FormatConverter

# CameraInteractor defines the type describes the logic of the camera's frame processing.
class CameraInteractor:
    _api: CameraAPI
    _format_conv: FormatConverter

    def __init__(self, api: CameraAPI):
        self._api = api
        self._format_conv = FormatConverter()


    # get_frame defines the logic of getting and encoding the frame.
    def get_frame(self, encoding: Formats) -> bytes | None:
        frame = self._api.read_frame()

        if encoding == Formats.PNG_FORMAT:
            return self._format_conv.convert_frame_to_png(frame)

        return None


    # close defines the logic of releasing the resources of the object.
    def close(self):
        self._api.close()
