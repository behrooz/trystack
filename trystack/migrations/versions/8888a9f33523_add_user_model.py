"""add user model

Revision ID: 8888a9f33523
Revises: 1de86c0cc4db
Create Date: 2023-01-01 17:22:13.604333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8888a9f33523'
down_revision = '1de86c0cc4db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('middlename', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('mobile', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('registeredAt', sa.DateTime(), nullable=False),
    sa.Column('lastLogin', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
