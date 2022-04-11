import requests
from requests import Response
from endpoints import api_endpoint
from src.models import User


def login(username):
    return requests.post(f'{api_endpoint}/login', json={
        'username': username
    }, headers={'Content-Type': 'application/json'}).json()


def info():
    response = requests.get(f'{api_endpoint}/info', headers={
        'Authorization': f'Bearer {User.token}'
    })
    if response.status_code != 200:
        pass

    return response.json()


def _error_handler(response: Response, f, *f_args):
    if response.status_code == 401:
        login(User.username)
        f(*f_args)
    else:
        pass  # handle
