"""create post table

Revision ID: 55bb9cb63723
Revises: 
Create Date: 2025-03-05 15:42:20.227557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55bb9cb63723'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("user_post",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column("title",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user_post")
