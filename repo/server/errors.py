import enum

# ServerErrorCodes defines the enum of the codes describes 
# the problems with the server interaction.
class ServerErrorCodes(enum.Enum):
    ERR_POST_REQUEST = 0
    ERR_SERVER_HANDLER = 1


# ServerErr defines the type of the server's errors that throws with the exception and
# describes the server interaction problems.
class ServerErr(BaseException):
    _code: ServerErrorCodes
    _message: str

    def __init__(self, msg: str, code: ServerErrorCodes):
        self._message = msg
        self._code = code


    def get_message(self) -> str:
        return self._message


    def get_code(self) -> ServerErrorCodes:
        return self._code
