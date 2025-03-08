"""adding few extra columns

Revision ID: 2eb94c32fe6d
Revises: 55bb9cb63723
Create Date: 2025-03-05 16:19:20.869918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2eb94c32fe6d'
down_revision: Union[str, None] = '55bb9cb63723'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("user_post",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user_post","content")
    pass
