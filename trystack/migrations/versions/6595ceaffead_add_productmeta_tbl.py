"""add productmeta tbl

Revision ID: 6595ceaffead
Revises: 29375b2ff7c2
Create Date: 2023-02-16 14:02:36.553641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6595ceaffead'
down_revision = '29375b2ff7c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_meta',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('key', sa.String(length=64), nullable=False),
    sa.Column('product_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_meta')
    # ### end Alembic commands ###