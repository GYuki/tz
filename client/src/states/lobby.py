from src.models import User
from src.services import info
from src.states.base import BaseState
from src.states.enums import StateEnums


class LobbyState(BaseState):
    def on_enter(self):
        info_result = info()
        User.username = info_result['username']
        User.items = info_result['items']
        User.balance = info_result['balance']
        print(User.print())
        self._print_commands()

    def handle(self, *args):
        if args[0] == 'buy':
            self.controller.change_state(StateEnums.Purchase)
        elif args[0] == 'sell':
            self.controller.change_state(StateEnums.Sell)
        else:
            print("no such command. try again")
            self._print_commands()

    def _print_commands(self):
        print('Print "buy" to get new items or "sell" to sell your items')
