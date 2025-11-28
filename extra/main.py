import logging
from app.app import App
from view.notify import Controller

if __name__ == "__main__":
    try:
        app = App(
            Controller(1, "localhost:8080")
        )
        app.run()
    except:
        pass
