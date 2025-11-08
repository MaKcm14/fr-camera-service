from app.config import App

from repo.camera.errors import *
from repo.camera.capi import CameraAPI

from services.camera.interactor import CameraInteractor
from services.converter import ConverterErr
from services.server.interactor import FlowInteractor

from view.view import InfoDisplayView

if __name__ == "__main__":
    appl = App(
        InfoDisplayView(
            FlowInteractor(
                CameraInteractor(
                    CameraAPI(1),
                ),
                server_socket="",
            ),
            read_delay=5,
        ),
    )

    try:
        appl.run()
    except KeyboardInterrupt:
        appl.close()
    
    except CameraAPIError | ConverterErr as c:
        appl.close()
        print(f"[ERROR]: {c.get_message}\n[CODE]: {c.get_code()}")
