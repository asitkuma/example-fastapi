"""add phone number to user table

Revision ID: 930d70206aec
Revises: d57c7c4e6e77
Create Date: 2025-03-06 12:00:32.004740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '930d70206aec'
down_revision: Union[str, None] = 'd57c7c4e6e77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user_registration",sa.Column("phone_number",sa.String(),nullable=False))
    op.create_unique_constraint("unique_key","user_registration",["phone_number"])


def downgrade() -> None:
    op.drop_column("user_registration","phone_number")