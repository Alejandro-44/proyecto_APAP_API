"""Update Employee model with additional fields

Revision ID: a4f5903942bc
Revises: 
Create Date: 2024-11-23 15:18:29.279164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4f5903942bc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('nationality', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('document_id', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('birth_date', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('city_of_residence', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('country_of_residence', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('profession', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('position', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('is_entrepreneur', sa.Boolean(), nullable=True))
    op.add_column('employees', sa.Column('entrepreneurship_name', sa.String(), nullable=True))
    op.alter_column('employees', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('employees', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'employees', ['document_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='unique')
    op.alter_column('employees', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('employees', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('employees', 'entrepreneurship_name')
    op.drop_column('employees', 'is_entrepreneur')
    op.drop_column('employees', 'position')
    op.drop_column('employees', 'profession')
    op.drop_column('employees', 'country_of_residence')
    op.drop_column('employees', 'city_of_residence')
    op.drop_column('employees', 'birth_date')
    op.drop_column('employees', 'gender')
    op.drop_column('employees', 'document_id')
    op.drop_column('employees', 'nationality')
    # ### end Alembic commands ###
