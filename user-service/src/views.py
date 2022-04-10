from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import create_access_token, jwt_required, current_user
from sqlalchemy.exc import IntegrityError

from database import db
from exceptions import InvalidUsage
from src.serializers import user_schema
from src import services

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/users', methods=('POST',))
@use_kwargs(user_schema)
@marshal_with(user_schema)
def login(username, **kwargs):
    try:
        user = services.get_user(username)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_already_registered()
    user.token = create_access_token(identity=user.username)

    return user


@blueprint.route('/api/users', methods=('GET',))
@jwt_required()
@marshal_with(user_schema)
def get_user():
    return current_user
