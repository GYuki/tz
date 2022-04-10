from marshmallow import Schema, fields, post_dump, pre_load


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    token = fields.Str(dump_only=True)

    @pre_load
    def make_user(self, data, **kwargs):
        return data

    @post_dump
    def dump_user(self, data, **kwargs):
        return data


user_schema = UserSchema()
