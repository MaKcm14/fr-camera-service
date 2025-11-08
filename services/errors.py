import enum

# ConverterErrorCodes defines the enum of the codes describes the problems with the data converting.
class ConverterErrorCodes(enum.Enum):
    PNG_CONVERT_ERR = 0


# ConverterErr defines the type of the converter's errors that throws with the exception and
# describes the data converting problems.
class ConverterErr(BaseException):
    _code: ConverterErrorCodes
    _message: str

    def __init__(self, msg: str, code: ConverterErrorCodes):
        self._message = msg
        self._code = code


    def get_message(self) -> str:
        return self._message


    def get_code(self) -> ConverterErrorCodes:
        return self._code
