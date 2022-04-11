from src.models import Item


def get_item_by_id(id):
    return Item.query.get(id)


def get_items():
    return Item.query.all()


def get_included_items(ids):
    return Item.query.filter(Item.id.in_(ids)).all()


def get_excluded_items(ids):
    return Item.query.filter(Item.id.notin_(ids)).all()
