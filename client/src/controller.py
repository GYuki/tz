from src.states.base import BaseState
from src.states.lobby import LobbyState
from src.states.login import LoginState


class Controller(object):
    def __init__(self):
        base_state = BaseState(self, 0)
        login_state = LoginState(self, 1)
        lobby_state = LobbyState(self, 2)
        self.states = {
            base_state.num: base_state,
            login_state.num: login_state,
            lobby_state.num: lobby_state
        }
        self.current_state = 0
        self.change_state(1)

    def change_state(self, state):
        self.states[self.current_state].on_exit()
        self.current_state = state
        self.states[self.current_state].on_enter()

    def handle(self, *args):
        self.states[self.current_state].handle(*args)
