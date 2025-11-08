import enum

# CameraAPIErrCodes defines the type of the errors' codes describes the problems with the
# camera interaction.
class CameraAPIErrCodes(enum.Enum):
    ERR_CONN = 0
    ERR_FRAME_READING = 2


# CameraAPIError defines the type of the errors that throws with the exception
# in cases of the camera interaction's errors.
class CameraAPIError(BaseException):
    _code: CameraAPIErrCodes
    _message: str

    def __init__(self, msg: str, code: CameraAPIErrCodes):
        self._code = code
        self._message = msg


    def get_message(self) -> str:
        return self._message


    def get_code(self) -> CameraAPIErrCodes:
        return self._code
