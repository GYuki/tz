from src.states.base import BaseState
from src.states.enums import StateEnums
from src.states.lobby import LobbyState
from src.states.login import LoginState
from src.states.purchase import PurchaseState
from src.states.sell import SellState


class Controller(object):
    def __init__(self):
        base_state = BaseState(self, StateEnums.Base)
        login_state = LoginState(self, StateEnums.Login)
        lobby_state = LobbyState(self, StateEnums.Lobby)
        purchase_state = PurchaseState(self, StateEnums.Purchase)
        sell_state = SellState(self, StateEnums.Sell)
        self.states = {
            base_state.num: base_state,
            login_state.num: login_state,
            lobby_state.num: lobby_state,
            purchase_state.num: purchase_state,
            sell_state.num: sell_state
        }
        self.current_state = StateEnums.Base
        self.change_state(StateEnums.Login)

    def change_state(self, state):
        self.states[self.current_state].on_exit()
        self.current_state = state
        self.states[self.current_state].on_enter()

    def handle(self, *args):
        self.states[self.current_state].handle(*args)
