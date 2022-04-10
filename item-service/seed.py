import json

from flask_seeder import Seeder, Faker, generator

from src.models import Item
from src.serializers import ItemSchema


class ItemSeeder(Seeder):
    def run(self):
        with open('seed.json') as file:
            json_items = json.load(file)

        items = ItemSchema(many=True).load(json_items)
        print(items)
