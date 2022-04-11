from src.models import User
from src.services import sell_item
from src.states.enums import StateEnums
from src.states.inventory import InventoryState


class SellState(InventoryState):
    def on_enter(self):
        print('What do you want to sell?')
        print(User.items)

    def handle(self, *args):
        if args[0] == 'b':
            super().handle(*args)
            return
        try:
            item_id = int(args[0])
        except ValueError:
            print('Print correct int')
            return

        sell_item(item_id)
        self.controller.change_state(StateEnums.Lobby)
