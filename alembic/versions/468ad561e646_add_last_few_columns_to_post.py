"""add last few columns to post

Revision ID: 468ad561e646
Revises: a736c9236cb9
Create Date: 2026-06-14 23:17:19.915548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '468ad561e646'
down_revision: Union[str, None] = 'a736c9236cb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column ("posts", sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP (timezone=True), nullable=False, server_default=sa.text
        ("NOW() " )),)
    pass



def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
