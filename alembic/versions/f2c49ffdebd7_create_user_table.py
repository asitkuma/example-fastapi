"""create user_table

Revision ID: f2c49ffdebd7
Revises: 2eb94c32fe6d
Create Date: 2025-03-05 16:48:51.061721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2c49ffdebd7'
down_revision: Union[str, None] = '2eb94c32fe6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("user_detail",sa.Column("id",sa.Integer(),nullable=False),sa.Column("email",sa.String(),nullable=False),sa.Column("password",sa.String(),nullable=False),sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False),sa.PrimaryKeyConstraint("id"),sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user_detail")
    pass
