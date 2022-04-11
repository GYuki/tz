from src.models import User
from src.services import info
from src.states.base import BaseState


class LobbyState(BaseState):
    def on_enter(self):
        info_result = info()
        User.username = info_result['username']
        User.items = info_result['items']
        User.balance = info_result['balance']
        print(User.print())
