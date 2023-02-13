"""create category dbl new fields

Revision ID: 22d0658781fb
Revises: c34c63a98dc3
Create Date: 2023-02-13 11:26:30.930981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22d0658781fb'
down_revision = 'c34c63a98dc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
