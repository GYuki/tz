from src.services import get_items_to_buy, buy_item
from src.states.enums import StateEnums
from src.states.inventory import InventoryState


class PurchaseState(InventoryState):
    def on_enter(self):
        print('What do you want to buy?')
        items_to_buy = get_items_to_buy()
        print(items_to_buy)

    def handle(self, *args):
        if args[0] == 'b':
            super().handle(*args)
            return
        try:
            item_id = int(args[0])
        except ValueError:
            print('Print correct int')
            return

        buy_item(item_id)
        self.controller.change_state(StateEnums.Lobby)
