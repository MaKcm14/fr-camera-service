from view.view import Controller

# App defines the main application's class.
class App:
    _contr: Controller

    def __init__(self, contr: Controller):
        self._contr = contr


    # run defines the logic of starting the application.
    def run(self):
        self._contr.run()
