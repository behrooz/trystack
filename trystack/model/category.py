from trystack.trystack import db
from trystack.util import uuidgen, now

class Category(db.Model):
    id=db.Column(db.String(64), primary_key=True, default=uuidgen)
    title=db.Column(db.String(75),nullable=False)
    metaTitle=db.Column(db.String(100),nullable=True)
    slug=db.Column(db.String(100),nullable=True)
    content=db.Column(db.Text)

