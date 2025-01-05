from flask import Flask, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from models.models import UserModels
from flask_smorest import Blueprint
import json

auth = Blueprint("auth", __name__)

SECRET_KEY = 'ahs!2!#@*231j'

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    provided_secret = data.get("secret")
    # username = data.get("username")
    # password = data.get("password")

    # user = UserModels.query.filter_by(username=username).first()
    # if not user or not check_password_hash(user.password, password):
        # return {"message": "Invalid Credentials"}
    
    # access_token = create_access_token(identity=user.id)
    access_token = create_access_token(identity=json.dumps({
        "role":"user",
        "permissions":"read-write"
    }))
    return {"access_token": access_token}, 200