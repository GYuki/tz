from flask import Blueprint, request

from src.services import get_item_ids_by_user_id

blueprint = Blueprint('user-item', __name__)


@blueprint.route('/api/user_items', methods=('GET',))
def get_user_items():
    user_id = int(request.args.get('user_id'))
    items = get_item_ids_by_user_id(user_id)
    return {
        'user': user_id,
        'items': items
    }
