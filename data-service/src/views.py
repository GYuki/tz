from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from sqlalchemy.exc import IntegrityError

from database import db
from exceptions import InvalidUsage
from src.serializers import user_data_schema
from src import services

blueprint = Blueprint('data', __name__)


@blueprint.route('/api/data', methods=('GET',))
@marshal_with(user_data_schema)
def get_user_data():
    player_id = int(request.args.get('player_id'))
    user_data = services.get_user_data(player_id)
    if not user_data:
        raise InvalidUsage.user_data_not_found()
    return user_data


@blueprint.route('/api/data', methods=('POST',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def create_user_data(player_id):
    try:
        user_data = services.create_user_data(player_id)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_data_already_registered()
    return user_data


@blueprint.route('/api/data', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def update_user_data(player_id, balance):
    try:
        user_data = services.update_user_data(player_id, balance)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_data_update_error()
    return user_data


@blueprint.route('/api/data/daily_bonus', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def daily_bonus(player_id):
    user = services.get_user_data(player_id)
    if user is None:
        try:
            user_data = services.create_user_data(player_id)
        except IntegrityError:
            db.session.rollback()
            raise InvalidUsage.user_data_update_error()
    try:
        user_data = services.change_balance(user, 100)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_data_update_error()
    return user_data


@blueprint.route('/api/data/give_money', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def give_money(player_id, balance):
    user = services.get_user_data(player_id)
    if user is None:
        raise InvalidUsage.user_data_not_found()
    try:
        user_data = services.change_balance(user, balance)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_data_update_error()
    return user_data


@blueprint.route('/api/data/take_money', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def take_money(player_id, balance):
    user = services.get_user_data(player_id)
    if user is None:
        raise InvalidUsage.user_data_not_found()
    if user.balance < -balance:
        raise InvalidUsage.not_enough_balance()
    try:
        user_data = services.change_balance(user, -balance)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_data_update_error()
    return user_data
