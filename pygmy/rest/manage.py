import datetime

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pygmy.config import config

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config.setdefault('JWT_ACCESS_TOKEN_EXPIRES', datetime.timedelta(**{'seconds': int(eval(config.access_token_expire_time_sec))}))
app.config.setdefault('JWT_REFRESH_TOKEN_EXPIRES', datetime.timedelta(**{'seconds': int(eval(config.refresh_token_expire_time_sec))}))
app.config.setdefault('JWT_HEADER_NAME', 'JWT_Authorization')
app.secret_key = config.secret

jwt = JWTManager(app)

# This import is required. Removing this will break all hell loose.
import pygmy.rest.urls as _


def run():
    app.run(host=config.host, port=int(config.port))
