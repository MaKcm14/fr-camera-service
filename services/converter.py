import cv2
import enum

from cv2.typing import MatLike
from services.errors import ConverterErr, ConverterErrorCodes

# Formats defines the enum of the possible converter's formats.
class Formats(enum.Enum):
    PNG_FORMAT = 0


# FormatConverter defines the type of the data format converter.
class FormatConverter:
    def convert_frame_to_png(self, data: MatLike) -> bytes:
        op: str = "services.converter"

        flag_encode_success, encoded_data = cv2.imencode(
            ".png", data, 
            [cv2.IMWRITE_PNG_STRATEGY_RLE, 3],
        )

        if flag_encode_success:
            return encoded_data.tobytes()

        raise ConverterErr(
                f"error of the {op}: error of encoding the frame",
                ConverterErrorCodes.PNG_CONVERT_ERR
        )