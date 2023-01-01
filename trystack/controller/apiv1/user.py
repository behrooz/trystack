from trystack.util import jsonify
from trystack.decorator import json_required
from trystack.model import user

class UserController():

    @json_required
    def register():
        #print("asasa")
        return jsonify(
            state={"register":"you are registered"},
            status=201
        )

    @json_required
    def login():
        return jsonify(
            {"login":"you are logedin"}
        )    