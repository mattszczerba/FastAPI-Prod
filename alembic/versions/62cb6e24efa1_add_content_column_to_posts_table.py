"""add content column to posts table

Revision ID: 62cb6e24efa1
Revises: ca0b42c26309
Create Date: 2022-04-09 11:04:05.075349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62cb6e24efa1'
down_revision = 'ca0b42c26309'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
