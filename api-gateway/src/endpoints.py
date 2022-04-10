import os

user_service = os.getenv('user-service', default='http://127.0.0.1:5000')
user_data_service = os.getenv('user_data_service', default='http://127.0.0.1:5001')
