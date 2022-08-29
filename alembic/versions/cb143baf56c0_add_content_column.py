"""Add content column

Revision ID: cb143baf56c0
Revises: f58f7c5140eb
Create Date: 2022-08-29 13:38:48.402829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb143baf56c0'
down_revision = 'f58f7c5140eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

# Usually contains what undoes the upgrade
def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
