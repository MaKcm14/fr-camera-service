import logging

from app.config import App

from repo.camera.errors import *
from repo.camera.capi import CameraAPI

from repo.server.server import APIServer

from services.camera.interactor import CameraInteractor
from services.converter import ConverterErr
from services.server.interactor import FlowInteractor

from view.view import Controller

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('./logs/fr-camera-service.log'),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(__name__)

    appl = App(
        Controller(
            FlowInteractor(
                CameraInteractor(
                    CameraAPI(0),
                    logger,
                ),
                APIServer("localhost:8080"),
                logger,
            ),
            read_delay=1,
        ),
    )

    try:
        appl.run()
    except:
        pass
