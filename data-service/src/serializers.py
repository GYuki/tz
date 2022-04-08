from marshmallow import Schema, fields, pre_load, post_dump


class UserDataSchema(Schema):
    player_id = fields.Int()
    balance = fields.Int()

    @pre_load
    def make_data(self, data, **kwargs):
        return data

    @post_dump
    def dump_data(self, data, **kwargs):
        return data


user_data_schema = UserDataSchema()
