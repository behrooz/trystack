from trystack.trystack import db
from trystack.util import uuidgen, now

class OrderItem(db.Model):
    
    id=db.Column(db.String(64), primary_key=True, nullable= False)
    sku=db.Column(db.String(100), nullable=False)
    price=db.Column(db.FLOAT,nullable=False)
    discount=db.Column(db.FLOAT, nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    createdAt=db.Column(db.DateTime,nullable=False)
    updatedAt=db.Column(db.DateTime,nullable=False)
    content=db.Column(db.DateTime,nullable=True)    
    product_id=db.Column(db.String(64), db.ForeignKey("product.id"))