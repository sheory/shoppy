"""create customer, address and bank_account table

Revision ID: e043cb94744a
Revises: 01291d1ca47d
Create Date: 2022-02-05 17:03:54.717320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e043cb94744a'
down_revision = '01291d1ca47d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('street', sa.VARCHAR(length=100), nullable=False),
    sa.Column('city', sa.VARCHAR(length=100), nullable=False),
    sa.Column('district', sa.VARCHAR(length=100), nullable=False),
    sa.Column('postal_code', sa.VARCHAR(length=100), nullable=False),
    sa.Column('country', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('bank_account',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('account', sa.INTEGER(), nullable=False),
    sa.Column('agency', sa.INTEGER(), nullable=False),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.Column('_deleted', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('customer',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('cpf', sa.VARCHAR(length=100), nullable=False),
    sa.Column('id_address', sa.INTEGER(), nullable=True),
    sa.Column('id_bank_account', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.Column('_deleted', sa.BOOLEAN(), nullable=True),
    sa.ForeignKeyConstraint(['id_address'], ['address.id']),
    sa.ForeignKeyConstraint(['id_bank_account'], ['bank_account.id']),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('address')
    op.drop_table('bank_account')
    op.drop_table('customer')
