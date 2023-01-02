from trystack.trystack import ma
from trystack.model import User
from marshmallow import validate

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field(required=True)
    firstname = ma.auto_field(required=True)
    middlename = ma.auto_field(required=False)
    lastname   = ma.auto_field(required=True) 
    mobile = ma.auto_field(required=False)
    email = ma.auto_field(required=True,validate=validate.Email(error="Not a valid email address"))
    password = ma.auto_field(required=True, validate=validate.Length(8))
    registeredAt = ma.auto_field(dump_only=True)
    lastLogin = ma.auto_field(dump_only=True)