CALL ..\env\Scripts\activate
set FLASK_APP=app
flask db init
flask db migrate
flask db upgrade
flask run --port=5000