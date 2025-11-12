import logging
from app.app import App
from view.notify import UserNotifDisplayView

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('../logs/extra-notifying-service.log'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    try:
        app = App(
            UserNotifDisplayView("localhost:8080")
        )
        app.run()
    except Exception as e:
        logger.error(f"error: {e}")