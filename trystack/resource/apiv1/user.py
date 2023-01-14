from flask_restful import Resource, request
from trystack.controller.apiv1 import UserController

class UserResource(Resource):
    def get(self):
        pass
    def post(self):
        url = request.url
        if "login" in url:
            return self.login()
        elif "register" in url:
            return self.register()
        elif "logout" in url:
            return self.logout()

    def patch(self):
        pass
    def delete(self):
        pass

    def register(self):
        return UserController.register()

    def login(self):
        return UserController.login()

    def logout(self):
        return UserController.logout()