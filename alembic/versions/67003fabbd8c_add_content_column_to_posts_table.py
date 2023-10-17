"""add content column to posts table

Revision ID: 67003fabbd8c
Revises: 2ec356840d3a
Create Date: 2023-10-16 15:44:46.442186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67003fabbd8c'
down_revision: Union[str, None] = '2ec356840d3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('posts','content')
