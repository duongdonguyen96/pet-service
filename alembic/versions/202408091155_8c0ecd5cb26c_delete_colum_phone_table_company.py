"""delete_colum_phone_table_company

Revision ID: 8c0ecd5cb26c
Revises: 871b869307e0
Create Date: 2024-08-09 11:55:28.430020+07:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c0ecd5cb26c'
down_revision: Union[str, None] = '871b869307e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'phone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('phone', sa.VARCHAR(length=12), autoincrement=False, nullable=True, comment='Số điện thoại'))
    # ### end Alembic commands ###