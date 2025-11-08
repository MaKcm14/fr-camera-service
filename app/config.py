from view.view import InfoDisplayView

# App defines the main application's class.
class App:
    _view: InfoDisplayView

    def __init__(self, view: InfoDisplayView):
        self._view = view


    # run defines the logic of starting the application.
    def run(self):
        self._view.run()


    # close defines the logic of releasing the resources of the application.
    def close(self):
        self._view.close()
