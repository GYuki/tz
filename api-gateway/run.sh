source ../env/Scripts/activate
export FLASK_APP=app

export user_service=http://127.0.0.1:5000
export user_data_service=http://127.0.0.1:5001
export user_item_service=http://127.0.0.1:5002
export item_service=http://127.0.0.1:5003

flask run --port=80