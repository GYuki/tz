CALL ..\env\Scripts\activate
set FLASK_APP=app

set user_service=http://127.0.0.1:5000
set user_data_service=http://127.0.0.1:5001
set user_item_service=http://127.0.0.1:5002
set item_service=http://127.0.0.1:5003

flask run --port=80