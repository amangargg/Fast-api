"""Add user table

Revision ID: a1ef04b5136c
Revises: 84a6e839a927
Create Date: 2026-06-14 18:42:16.980701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1ef04b5136c'
down_revision: Union[str, None] = '84a6e839a927'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(' users',
                    sa.Column ('id', sa. Integer(), nullable=False),
                    sa.Column ('email', sa.String(), nullable=False),
                    sa.Column ('password', sa. String(), nullable=False),
                    sa.Column ('created_at', sa. TIMESTAMP (timezone=True),
                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
