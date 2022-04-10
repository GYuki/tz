import requests


def token_checker(headers):
    def wrap(f):
        def function_wrapper(*args):
            response = requests.get('http://127.0.0.1:5000/api/users', headers=headers)
            if response.status_code != 200:
                return  # error

            data = response.json()
            return f(data['id'], *args)
        return function_wrapper
    return wrap
