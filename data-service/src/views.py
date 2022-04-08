from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required
from marshmallow import fields
from sqlalchemy.exc import IntegrityError

from database import db
from src.serializers import user_data_schema
from src import services

blueprint = Blueprint('data', __name__)


@blueprint.route('/api/data', methods=('GET',))
@jwt_required
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def get_user_data(player_id):
    user_data = services.get_user_data(player_id)
    if not user_data:
        return  # 404
    return user_data


@blueprint.route('/api/data', methods=('POST',))
@jwt_required
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def create_user_data(player_id):
    try:
        user_data = services.create_user_data(player_id)
    except IntegrityError:
        db.session.rollback()
        return
    return user_data
