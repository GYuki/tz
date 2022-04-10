from src.services import get_user


def user_loader(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return get_user(identity)
