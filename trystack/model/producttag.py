from trystack.trystack import db
from trystack.util import uuidgen,now

class ProductTag(db.Model):

    id=db.Column(db.String(64), primary_key=True, default=uuidgen)    
    product_id = db.Column(db.String(64), db.ForeignKey('product.id'))
    tag_id = db.Column(db.String(64), db.ForeignKey('tag.id'))