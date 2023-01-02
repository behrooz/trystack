from flask import request
from trystack.util import jsonify
from trystack.decorator import json_required
from trystack.model import User
from trystack.scehma.apiv1 import UserSchema

class UserController():

    @json_required
    def register():
        user_schema = UserSchema(only=["username","middlename", "firstname", "lastname","mobile", "email","password"])
        request_data = user_schema.load(request.get_json())
        return jsonify(
            state=request_data,
            status=201
        )

    @json_required
    def login():
        return jsonify(
            {"login":"you are logedin"}
        )    