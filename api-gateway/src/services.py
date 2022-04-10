import requests
from flask import Response, request

from src.endpoints import user_item_service, item_service, user_data_service, user_service


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


def get_info(user):
    item_ids_response = requests.get(f'{user_item_service}/api/user_items?user_id={user["id"]}')
    if item_ids_response.status_code != 200:
        return _make_error_response(item_ids_response)
    item_ids = item_ids_response.json()

    item_objects_response = requests.get(
        f'{item_service}/api/items?ids={",".join(str(id) for id in item_ids["items"])}')
    if item_objects_response.status_code != 200:
        return _make_error_response(item_objects_response)
    item_objects = item_objects_response.json()

    user_data_response = requests.get(f'{user_data_service}/api/data?player_id={user["id"]}')
    if user_data_response.status_code != 200:
        return _make_error_response(user_data_response)
    user_data = user_data_response.json()

    return {
        'user_id': user['id'],
        'username': user['username'],
        'balance': user_data['balance'],
        'items': item_objects
    }


def purchase_item(user, item_id):
    item_response = requests.get(f'{item_service}/api/item?id={item_id}')
    if item_response.status_code != 200:
        return _make_error_response(item_response)

    if _take_money(user['id'], item_response.json()['price']).status_code != 200:
        print('shut money')
        return  # raise error

    if _add_item(user['id'], item_id).status_code != 200:
        # rollback transaction
        print('rollback')
        if _give_money(user['id'], item_response.json()['price']):
            print('could not give money')
            return  # raise error

    return {
        'status': True
    }


def _add_item(user_id, item_id):
    return requests.post(f'{user_item_service}/api/user_items', json={
        'user_id': user_id,
        'item_id': item_id
    }, headers=request.headers)


def _take_money(user_id, balance):
    return requests.put(f'{user_data_service}/api/data/take_money', json={
        'player_id': user_id,
        'balance': balance
    }, headers=request.headers)


def _give_money(user_id, balance):
    return requests.put(f'{user_data_service}/api/data/give_money', json={
        'player_id': user_id,
        'balance': balance
    }, headers=request.headers)


def _make_error_response(response):
    return Response(response.content, response.status_code)
