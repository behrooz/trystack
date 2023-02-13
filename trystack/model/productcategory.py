from trystack.trystack import db
from trystack.util import uuidgen,now

class ProjectCategory(db.Model):

    id=db.Column(db.String(64), primary_key=True, default=uuidgen)
    category_id=db.Column(db.ForeignKey("category.id"))        
    #parent= db.relationship("Category", backref="children")                