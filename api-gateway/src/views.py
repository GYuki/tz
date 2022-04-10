import requests
from flask import Blueprint, request, Response

from src.endpoints import user_service, user_data_service
from wrappers import token_checker
from src import services

blueprint = Blueprint('api-gateway', __name__)


@blueprint.route('/login', methods=('POST',))
def login():
    return services.login()


@blueprint.route('/info', methods=('GET',))
@token_checker
def get_info(user):
    return services.get_info(user)
