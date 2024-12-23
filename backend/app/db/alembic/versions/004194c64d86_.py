"""empty message

Revision ID: 004194c64d86
Revises: 437824534429
Create Date: 2024-12-02 20:40:22.598038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '004194c64d86'
down_revision: Union[str, None] = '437824534429'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charactertable',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('owner_id', sa.Uuid(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['usertable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('charactertable')
    # ### end Alembic commands ###
