from flask import Flask
from flask_smorest import Api
from resources.books import blp as BooksBlueprint
from db import db
import models
import os
from flask_jwt_extended import JWTManager
from resources.auth import auth

def create_app(db_url=None):
    app = Flask(__name__) 

    app.config["PROPOGATE_EXCEPTION"]  = True
    app.config["API_TITLE"] = "Book REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABSE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config["JWT_SECRET_KEY"] = 'ahs!2!#@*231j'
    db.init_app(app)
    JWTManager(app)
    with app.app_context():
        db.create_all()

    api = Api(app)

    api.register_blueprint(BooksBlueprint)
    app.register_blueprint(auth)

    return app