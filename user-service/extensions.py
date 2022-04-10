from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from utils import user_loader

jwt = JWTManager()
migrate = Migrate()


jwt.user_lookup_loader(user_loader)
