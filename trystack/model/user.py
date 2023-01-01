from trystack.trystack import db
from trystack.util import uuidgen, now
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True,default=uuidgen)
    username = db.Column(db.String(50),nullable=False)
    firstname = db.Column(db.String(50),nullable=False)
    middlename = db.Column(db.String(50),nullable=False)
    lastname  = db.Column(db.String(50),nullable=False)
    mobile = db.Column(db.String(15),nullable=True)
    email = db.Column(db.String(50),nullable=False,unique=True,index=True)
    password = db.Column(db.String(32),nullable=False)
    registeredAt = db.Column(db.DateTime,nullable=False, default=now)
    lastLogin = db.Column(db.DateTime,nullable=True)
    

