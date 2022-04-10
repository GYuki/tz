from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_DATA_NOT_FOUND = template(['User data not found'], code=404)
USER_DATA_ALREADY_REGISTERED = template(['User data already registered'], code=422)
USER_DATA_UPDATE_ERROR = template(['User data update error'], code=422)
NOT_ENOUGH_BALANCE = template(['Not enough balance error'], code=500)


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
    def user_data_not_found(cls):
        return cls(**USER_DATA_NOT_FOUND)

    @classmethod
    def user_data_already_registered(cls):
        return cls(**USER_DATA_ALREADY_REGISTERED)

    @classmethod
    def user_data_update_error(cls):
        return cls(**USER_DATA_UPDATE_ERROR)

    @classmethod
    def not_enough_balance(cls):
        return cls(**NOT_ENOUGH_BALANCE)
