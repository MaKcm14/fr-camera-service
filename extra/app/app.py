from view.notify import Controller

class App:
    _contr: Controller

    def __init__(self, contr: Controller):
        self._contr = contr

    def run(self):
        self._contr.run()
