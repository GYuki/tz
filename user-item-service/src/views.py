from flask import Blueprint, request
from flask_apispec import use_kwargs
from sqlalchemy.exc import IntegrityError

from src.serializers import user_item_data
from src import services

blueprint = Blueprint('user-item', __name__)


@blueprint.route('/api/user_item', methods=('GET',))
def get_user_item():
    user_id = int(request.args.get('user_id'))
    item_id = int(request.args.get('item_id'))
    item = services.get_item(user_id=user_id, item_id=item_id)
    if item is None:
        return  # return 404
    return item


@blueprint.route('/api/user_items', methods=('GET',))
def get_user_items():
    user_id = int(request.args.get('user_id'))
    items = services.get_item_ids_by_user_id(user_id)
    return {
        'user': user_id,
        'items': items
    }


@blueprint.route('/api/user_items', methods=('POST',))
@use_kwargs(user_item_data)
def add_item_to_user(user_id, item_id):
    try:
        services.add_item_to_user(user_id, item_id)
    except IntegrityError:
        print('ERROR')
        return  # return exc

    print('SUCCESS')
    return {
        "success": True
    }


@blueprint.route('/api/user_items', methods=('DELETE',))
@use_kwargs(user_item_data)
def remove_item_from_user(user_id, item_id):
    result = services.remove_item_from_user(user_id, item_id)
    if not result:
        return  # 404
    return
