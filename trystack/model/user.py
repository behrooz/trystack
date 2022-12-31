from trystack.trystack import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    firstname = db.Column(db.String(50),nullable=False)
    middlename= db.Column(db.String(50),nullable=False)
    lastname  = db.Column(db.String(50))
    mobile=db.Column(db.String(15),nullable=True)
    email=db.Column(db.String(50),nullable=False,unique=True,index=True)
    password=db.Column(db.String(32),nullable=False)
    registeredAt=db.Column(db.DateTime,nullable=False)
    lastLogin=db.Column(db.DateTime,nullable=False)
    

