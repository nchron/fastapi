"""Create posts table

Revision ID: f58f7c5140eb
Revises: 
Create Date: 2022-08-29 13:31:07.720881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f58f7c5140eb'
down_revision = None
branch_labels = None
depends_on = None

# Handels chages
def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass

# Handels rollback
def downgrade() -> None:
    op.drop_table('posts')
    pass
