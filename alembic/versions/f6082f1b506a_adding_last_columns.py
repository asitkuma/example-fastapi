"""adding last columns

Revision ID: f6082f1b506a
Revises: fc5a31f01ebd
Create Date: 2025-03-05 18:26:35.158660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6082f1b506a'
down_revision: Union[str, None] = 'fc5a31f01ebd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("user_post",sa.Column("is_published",sa.Boolean(),nullable=False,server_default="TRUE"))
    op.add_column("user_post",sa.Column("time_at_created",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("NOW()")))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user_post","is_published")
    op.drop_column("user_post","time_at_created")
    pass
