from src.services import get_items_to_buy, buy_item
from src.states.base import BaseState
from src.states.enums import StateEnums


class PurchaseState(BaseState):
    def on_enter(self):
        print('What do you want to buy?')
        items_to_buy = get_items_to_buy()
        print(items_to_buy)

    def handle(self, *args):
        try:
            item_id = int(args[0])
        except ValueError:
            print('Print correct int')
            return

        buy_item(item_id)
        self.controller.change_state(StateEnums.Lobby)
