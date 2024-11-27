"""empty message

Revision ID: cc47fff5107a
Revises: c59bfea12e0e
Create Date: 2024-11-27 22:44:53.595996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = 'cc47fff5107a'
down_revision: Union[str, None] = 'c59bfea12e0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
