from src.models import Item


def get_item_by_id(id):
    return Item.query.get(id)


def get_items(ids, limit, offset):
    return Item.query.filter(Item.id.in_(ids)).offset(offset).limit(limit).all()
