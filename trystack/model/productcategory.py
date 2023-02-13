from trystack.trystack import db
from trystack.util import uuidgen,now

class ProductCategory(db.Model):

    id=db.Column(db.String(64), primary_key=True, default=uuidgen)    
    product_id = db.Column(db.String(64), db.ForeignKey('product.id'))