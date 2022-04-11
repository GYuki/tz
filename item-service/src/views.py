from flask import Blueprint, request
from flask_apispec import marshal_with

from exceptions import InvalidUsage
from src.serializers import item_schema, items_schema
from src import services

blueprint = Blueprint('item', __name__)


@blueprint.route('/api/item', methods=('GET',))
@marshal_with(item_schema)
def get_item():
    item_id = int(request.args.get('id'))
    item = services.get_item_by_id(item_id)
    if item is None:
        raise InvalidUsage.item_not_found()
    return item


@blueprint.route('/api/items', methods=('GET',))
@marshal_with(items_schema)
def get_items():
    return services.get_items()


@blueprint.route('/api/included_items', methods=('GET',))
@marshal_with(items_schema)
def get_included_items():
    item_ids = request.args.get('ids').split(',')
    return services.get_included_items(item_ids)


@blueprint.route('/api/excluded_items', methods=('GET',))
@marshal_with(items_schema)
def get_excluded_items():
    item_ids = request.args.get('ids').split(',')
    return services.get_excluded_items(item_ids)
