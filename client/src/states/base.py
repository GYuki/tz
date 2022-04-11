class BaseState(object):
    def __init__(self, controller, num):
        self.controller = controller
        self.num = num

    def on_enter(self):
        pass

    def handle(self, *args):
        pass

    def on_exit(self):
        pass
