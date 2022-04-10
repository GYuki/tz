from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_ITEM_ALREADY_EXISTS = template(['User item already exists'], code=422)
USER_ITEM_NOT_FOUND = template(['User item not found'], code=404)


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def user_item_already_exists(cls):
        return cls(**USER_ITEM_ALREADY_EXISTS)

    @classmethod
    def user_item_not_found(cls):
        return cls(**USER_ITEM_NOT_FOUND)
