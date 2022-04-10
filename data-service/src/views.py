from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from sqlalchemy.exc import IntegrityError

from database import db
from src.serializers import user_data_schema
from src import services

blueprint = Blueprint('data', __name__)


@blueprint.route('/api/data', methods=('GET',))
@marshal_with(user_data_schema)
def get_user_data():
    player_id = int(request.args.get('player_id'))
    user_data = services.get_user_data(player_id)
    if not user_data:
        return  # 404
    return user_data


@blueprint.route('/api/data', methods=('POST',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def create_user_data(player_id):
    try:
        user_data = services.create_user_data(player_id)
    except IntegrityError:
        db.session.rollback()
        return
    return user_data


@blueprint.route('/api/data', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def update_user_data(player_id, balance):
    try:
        user_data = services.update_user_data(player_id, balance)
    except IntegrityError:
        db.session.rollback()
        return
    return user_data


@blueprint.route('/api/data/daily_bonus', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def daily_bonus(player_id):
    user = services.get_user_data(player_id)
    if user is None:
        return  # raise 404
    try:
        user_data = services.change_balance(player_id, 100)
    except IntegrityError:
        db.session.rollback()
        return
    return user_data


@blueprint.route('/api/data/purchase', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def purchase_item(player_id, price):
    user = services.get_user_data(player_id)
    if user is None:
        return  # raise 404
    if user.balance < price:
        return  # raise no balance
    try:
        user_data = services.change_balance(player_id, price)
    except IntegrityError:
        db.session.rollback()
        return
    return user_data


@blueprint.route('/api/data/sell', methods=('PUT',))
@use_kwargs(user_data_schema)
@marshal_with(user_data_schema)
def sell_item(player_id, price):
    user = services.get_user_data(player_id)
    if user is None:
        return  # raise 404
    try:
        user_data = services.change_balance(player_id, price)
    except IntegrityError:
        db.session.rollback()
        return
    return user_data
