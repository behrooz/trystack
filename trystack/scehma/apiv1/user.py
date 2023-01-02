from trystack.trystack import ma
from trystack.model import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    firstname = ma.auto_field()
    middlename = ma.auto_field()
    lastname   = ma.auto_field() 
    mobile = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    registeredAt = ma.auto_field(dump_only=True)
    lastLogin = ma.auto_field(dump_only=True)