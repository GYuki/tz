from flask import Blueprint, request
from flask_apispec import marshal_with

from src.serializers import item_schema, items_schema
from src import services

blueprint = Blueprint('item', __name__)


@blueprint.route('/api/item', methods=('GET',))
@marshal_with(item_schema)
def get_item():
    item_id = int(request.args.get('id'))
    item = services.get_item_by_id(item_id)
    if item is None:
        return  # 404
    return item


@blueprint.route('/api/items', methods=('GET',))
@marshal_with(items_schema)
def get_items():
    item_ids = request.args.get('ids').split(',')
    limit = request.args.get('limit', 20)
    offset = request.args.get('offset', 0)
    return services.get_items(item_ids, limit, offset)
