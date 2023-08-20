"""Adding Expense model

Revision ID: 77bbce317c28
Revises: fa882fa3a039
Create Date: 2023-08-20 16:01:01.437300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77bbce317c28'
down_revision: Union[str, None] = 'fa882fa3a039'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('expense_id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('cost_category', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.trip_id'], name=op.f('fk_expenses_trip_id_trips')),
    sa.PrimaryKeyConstraint('expense_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expenses')
    # ### end Alembic commands ###
