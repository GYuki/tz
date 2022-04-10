from src.models import UserItem


def get_item_ids_by_user_id(user_id):
    return [x.item_id for x in UserItem.query.filter_by(user_id=user_id)]
