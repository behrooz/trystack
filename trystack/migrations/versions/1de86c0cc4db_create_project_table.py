"""create project table

Revision ID: 1de86c0cc4db
Revises: 
Create Date: 2022-12-31 14:06:50.432976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1de86c0cc4db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_project_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_name'))

    op.drop_table('project')
    # ### end Alembic commands ###
