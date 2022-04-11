source ../env/Scripts/activate
export FLASK_APP=app
flask db init
flask db migrate
flask db upgrade
flask run --port=5003