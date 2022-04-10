import requests
from flask import request, Response

from src.endpoints import user_service


def token_checker(f):
    def function_wrapper(*args):
        response = requests.get(f'{user_service}/api/users', headers=request.headers)
        if response.status_code != 200:
            return Response(response.content, response.status_code)

        data = response.json()
        return f(data, *args)
    function_wrapper.__name__ = f.__name__
    return function_wrapper

