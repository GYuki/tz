import json

from flask_seeder import Seeder
from src.models import Item


class ItemSeeder(Seeder):
    def run(self):
        with open('./seeds/seed.json') as file:
            json_items = json.load(file)

        for item in json_items:
            Item(item['name'], item['price']).save()
