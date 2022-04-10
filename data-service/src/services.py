from src.models import UserData


def get_user_data(player_id):
    return UserData.query.filter_by(player_id=player_id).first()


def create_user_data(player_id):
    return UserData(player_id).save()


def update_user_data(player_id, balance):
    user = get_user_data(player_id)
    if user is None:
        return None
    user.update(player_id=player_id, balance=balance)
    return user


def change_balance(player_id, balance):
    user = get_user_data(player_id)
    if user is None:
        return None
    user.update(balance=balance+user.balance)
    return user
