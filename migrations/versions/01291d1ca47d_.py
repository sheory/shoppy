"""create product table

Revision ID: 01291d1ca47d
Revises: 
Create Date: 2022-02-01 00:27:09.627574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01291d1ca47d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('product')
