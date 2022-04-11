from src.states.base import BaseState
from src.states.enums import StateEnums


class InventoryState(BaseState):
    def handle(self, *args):
        self.controller.change_state(StateEnums.Lobby)
