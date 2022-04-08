from src.models import User


def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username).save()
    return user
