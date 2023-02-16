from trystack.trystack import db
from trystack.util import uuidgen,now

class ProductMeta(db.Model):

    id=db.Column(db.String(64),primary_key=True,default=uuidgen)
    key=db.Column(db.String(64),nullable=False)
    product_id=db.Column(db.String(64),db.ForeignKey('product.id'))