"""add senha em usuario

Revision ID: 0db4d7ae3102
Revises: ebaa66c9817b
Create Date: 2023-12-19 17:21:38.735304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0db4d7ae3102'
down_revision: Union[str, None] = 'ebaa66c9817b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('senha', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'senha')
    # ### end Alembic commands ###
