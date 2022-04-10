import requests
from flask import Blueprint, request, Response

from src.endpoints import user_service, user_data_service, user_item_service, item_service
from wrappers import token_checker

blueprint = Blueprint('api-gateway', __name__)


@blueprint.route('/login', methods=('POST',))
def login():
    login_response = requests.post(f'{user_service}/api/users', data=request.data, headers=request.headers)
    if login_response.status_code != 200:
        return Response(login_response.content, login_response.status_code)
    user = login_response.json()

    requests.put(
        f'{user_data_service}/api/data/daily_bonus',
        json={'player_id': user['id']},
        headers=request.headers
    )

    return user


@blueprint.route('/info', methods=('GET',))
@token_checker
def get_info(user):
    item_ids_response = requests.get(f'{user_item_service}/api/user_items?user_id={user["id"]}')
    if item_ids_response.status_code != 200:
        return Response(item_ids_response.content, item_ids_response.status_code)
    item_ids = item_ids_response.json()

    item_objects_response = requests.get(f'{item_service}/api/items?ids={",".join(str(id) for id in item_ids["items"])}')
    if item_objects_response.status_code != 200:
        return Response(item_objects_response.content, item_objects_response.status_code)
    item_objects = item_objects_response.json()

    user_data_response = requests.get(f'{user_data_service}/api/data?player_id={user["id"]}')
    if user_data_response.status_code != 200:
        return Response(user_data_response.content, item_objects_response.status_code)
    user_data = user_data_response.json()

    return {
        'user_id': user['id'],
        'balance': user_data['balance'],
        'items': item_objects
    }
