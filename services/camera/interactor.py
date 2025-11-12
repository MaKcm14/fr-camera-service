from logging import Logger
from repo.camera.capi import CameraAPI
from services.converter import Formats, FormatConverter
from services.errors import ConverterErr

# CameraInteractor defines the type describes the logic of the camera's frame processing.
class CameraInteractor:
    _api: CameraAPI
    _format_conv: FormatConverter
    _logger: Logger

    def __init__(self, api: CameraAPI, log: Logger):
        self._api = api
        self._format_conv = FormatConverter()
        self._logger = log


    # get_frame defines the logic of getting and encoding the frame.
    def get_frame(self, encoding: Formats) -> bytes | None:
        frame = self._api.read_frame()

        try:
            if encoding == Formats.PNG_FORMAT:
                    return self._format_conv.convert_frame_to_png(frame)
        except ConverterErr as c:
            self._logger.error(f"error of the converter: {c.get_message()}")

        return None


    # close defines the logic of releasing the resources of the object.
    def close(self):
        self._api.close()
