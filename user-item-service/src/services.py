from src.models import UserItem


def get_item_ids_by_user_id(user_id):
    return [x.item_id for x in UserItem.query.filter_by(user_id=user_id)]


def add_item_to_user(user_id, item_id):
    UserItem(user_id, item_id).save()


def remove_item_from_user(user_id, item_id):
    user_item = UserItem.query.filter_by(user_id=user_id, item_id=item_id).first()
    if user_item is None:
        return False
    user_item.delete()
    return True
