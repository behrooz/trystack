from trystack.trystack import db
from trystack.util import uuidgen, now

class Product(db.Model):

    id=db.Column(db.String(64), primary_key=True,default=uuidgen)
    userId=db.Column(db.String(64),nullable=False)
    title=db.Column(db.String(64),nullable=False)
    metaTile=db.Column(db.String(64),nullable=True)
    slug=db.Column(db.String(64),nullable=False)
    summary=db.Column(db.Text,nullable=False)    
    price=db.Column(db.String(64),nullable=False)
    discount=db.Column(db.String(64),nullable=False)
    quantity=db.Column(db.String(64),nullable=False)    
    createdAt=db.Column(db.DateTime,nullable=True,default=now)
    updateAt=db.Column(db.DateTime,nullable=True)
    publishedAt=db.Column(db.DateTime,nullable=True)
    content=db.Column(db.Text,nullable=True)    
    categories = db.relationship('ProductCategory', backref='Product')
    tags = db.relationship('ProductTag', backref='Product')
    orders=db.relationship('OrderItem', backref='Product')
    metas=db.relationship('ProductMeta',backref='Product')