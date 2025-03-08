"""add_foreign_key_Constraint

Revision ID: fc5a31f01ebd
Revises: f2c49ffdebd7
Create Date: 2025-03-05 17:47:13.725448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc5a31f01ebd'
down_revision: Union[str, None] = 'f2c49ffdebd7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("user_post",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("owner_id_fk","user_post","user_detail",["owner_id"],["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user_post","owner_id")
    pass