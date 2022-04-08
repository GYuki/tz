from marshmallow import Schema, fields, pre_load, post_dump


class ItemSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Int()

    @pre_load
    def make_item(self, item, **kwargs):
        return item

    @post_dump
    def dump_item(self, item, **kwargs):
        return item


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
