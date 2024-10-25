"""Init

Revision ID: dd76335cc82e
Revises: 
Create Date: 2024-10-15 20:33:51.896703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd76335cc82e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=100), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('flat_number', sa.Integer(), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('publishers', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'publishers', 'addresses', ['address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'publishers', type_='foreignkey')
    op.drop_column('publishers', 'address_id')
    op.drop_table('addresses')
    # ### end Alembic commands ###
