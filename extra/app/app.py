from view.notify import UserNotifDisplayView

class App:
    _view: UserNotifDisplayView

    def __init__(self, view: UserNotifDisplayView):
        self._view = view

    def run(self):
        self._view.start()
