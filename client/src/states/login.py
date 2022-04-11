from src.models import User
from src.services import login
from src.states.base import BaseState
from src.states.enums import StateEnums


class LoginState(BaseState):
    def on_enter(self):
        print('Enter username to start')

    def handle(self, *args):
        username = args[0]
        login_response = login(username)
        User.token = login_response['token']
        self.controller.change_state(StateEnums.Lobby)
