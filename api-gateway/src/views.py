import requests
from flask import Blueprint, request

from src.endpoints import user_service, user_data_service

blueprint = Blueprint('api-gateway', __name__)


@blueprint.route('/login', methods=('POST',))
def login():
    login_response = requests.post(f'{user_service}/api/users', data=request.data, headers=request.headers)
    if login_response.status_code != 200:
        return  # error
    user = login_response.json()

    daily_bonus = requests.put(
        f'{user_data_service}/api/data/daily_bonus',
        json={'player_id': user['id']},
        headers=request.headers
    )
    print(daily_bonus.status_code)

    return user
