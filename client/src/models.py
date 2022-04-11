class User(object):
    username: str = ''
    balance: int = 0
    token: str = ''
    items = None

    @classmethod
    def print(cls):
        return f'Username: {cls.username}\nBalance: {cls.balance}\nItems:{cls.items}'
