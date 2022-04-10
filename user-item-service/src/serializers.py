from marshmallow import Schema, fields, pre_load


class UserItemSchema(Schema):
    user_id = fields.Int()
    item_id = fields.Int()

    @pre_load
    def dump_data(self, data, **kwargs):
        return data


user_item_data = UserItemSchema()
