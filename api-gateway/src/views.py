from flask import Blueprint, request

from wrappers import token_checker
from src import services

blueprint = Blueprint('api-gateway', __name__)


@blueprint.route('/login', methods=('POST',))
def login():
    return services.login()


@blueprint.route('/info', methods=('GET',))
@token_checker
def get_info(user):
    return services.get_info(user)


@blueprint.route('/purchase', methods=('POST',))
@token_checker
def purchase_item(user):
    item_id = request.json['item_id']
    return services.purchase_item(user, item_id)


@blueprint.route('/sell', methods=('POST',))
@token_checker
def sell_item(user):
    item_id = request.json['item_id']
    return services.sell_item(user, item_id)
