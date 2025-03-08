"""auto-vote

Revision ID: d57c7c4e6e77
Revises: f6082f1b506a
Create Date: 2025-03-06 11:32:03.709052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd57c7c4e6e77'
down_revision: Union[str, None] = 'f6082f1b506a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("user_vote",
                    sa.Column("user_id",sa.Integer(),nullable=False),
                    sa.Column("post_id",sa.Integer(),nullable=False),
                    sa.PrimaryKeyConstraint("user_id","post_id"),
                    sa.ForeignKeyConstraint(["user_id"],["user_registration.id"],ondelete="CASCADE",onupdate="CASCADE"),
                    sa.ForeignKeyConstraint(["post_id"],["user_post.id"],ondelete="CASCADE",onupdate="CASCADE")
                    )
    


def downgrade() -> None:
    op.drop_table("user_vote")
    """Downgrade schema."""
