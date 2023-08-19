from flask import request
from trystack.util import jsonify
from trystack.decorator import json_required
from trystack.model import User
from trystack.config import Config
from trystack.scehma.apiv1 import UserSchema, LoginSchema
from trystack.trystack import db
from os import environ
import hashlib, json, jwt,redis
from marshmallow import INCLUDE

class UserController():

    @json_required
    def register():
        user_schema = UserSchema(only=["username","middlename", "firstname", "lastname","mobile", "email","password"])        
        request_data = ""
        try:
            request_data = user_schema.load(request.get_json())
            user = User.query.filter_by(email=request_data["email"]).first()
            if user is not None:
                return jsonify(
                    state= {"message": "username exists"},
                    status=403
                )
            password = hashlib.md5(request_data["password"].encode('utf-8')).hexdigest()
            user = User(
                username = request_data["username"],
                middlename= request_data["middlename"],
                firstname= request_data["firstname"],
                lastname= request_data["lastname"],
                mobile= request_data["mobile"],
                email= request_data["email"],
                password=password)
            db.session.add(user)
            db.session.commit()

        except Exception as e:
            return jsonify(
                state=e.messages,
                status=403
            )
        
        return jsonify(
            state=request_data,
            status=201
        )

    @json_required
    def login():        
        login_schema = LoginSchema(only=["email","password"])
        request_data = login_schema.load(request.get_json(),unknown=INCLUDE)
        user = User.query.filter_by(email=request_data.email).first()
        if user is None:
            return jsonify(
                state= {"user":"username or password is invalid"},
                status= 501
            )
        password = hashlib.md5(request_data.password.encode("utf-8")).hexdigest()
        if password == user.password:
            encoded_jwt = jwt.encode({"email":user.email}, "secret", algorithm="HS256")

            try:
              connection = redis.from_url(Config.CACHE_REDIS_HOST)
              connection.delete(user.email)
              connection.append(user.email,encoded_jwt)
              connection.close()
            except:
              return jsonify(
                state= {"token":encoded_jwt},
                status= 200
              )
        return jsonify(
            {"token": encoded_jwt}
        )

    @json_required    
    def logout():
        request_data = request.get_json()
        if "token" in request_data:
            jwt = request_data["token"]
            email = request_data["email"]
            connection = redis.from_url(Config.CACHE_REDIS_HOST,decode_responses='utf-8')            
            cache_token = connection.get(email)        
            if cache_token is not None and cache_token == jwt:
                connection.delete(email)
                return jsonify(
                    state= {"logout": "successfully logout"}
                )

            return jsonify(
                state= {"error": "token is not valid"}
            )
        return jsonify(
                state = {"error": "token is not present"}
            )
        #print(jwt,email)
