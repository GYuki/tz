import os

user_service = os.getenv('user_service', default='http://127.0.0.1:5000')
user_data_service = os.getenv('user_data_service', default='http://127.0.0.1:5001')
user_item_service = os.getenv('user_item_service', default='http://127.0.0.1:5002')
item_service = os.getenv('item_service', default='http://127.0.0.1:5003')
