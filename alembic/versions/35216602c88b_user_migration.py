"""Initial Migration

Revision ID: 061576d371b4
Revises: 
Create Date: 2024-09-05 23:33:38.949175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '061576d371b4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), index=True),
        sa.Column('email', sa.String(), unique=True, index=True),
        sa.Column('password', sa.String(), index=True)
    )

def downgrade() -> None:
    op.drop_table('users')
