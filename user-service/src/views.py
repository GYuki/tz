from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

from database import db
from src.models import User
from src.serializers import user_schema
from src.services import get_user

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/users', methods=('POST',))
@use_kwargs(user_schema)
@marshal_with(user_schema)
def login(username, **kwargs):
    try:
        user = get_user(username)
    except IntegrityError:
        db.session.rollback()
        return  # return error
    user.token = create_access_token(identity=user.id)

    return user
