"""create widgets

Revision ID: 9afc305078b8
Revises:
Create Date: 2018-07-22 09:53:22.761064

"""
from alembic import op
import sqlalchemy as sa


revision = '9afc305078b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'widgets',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('widgets')
