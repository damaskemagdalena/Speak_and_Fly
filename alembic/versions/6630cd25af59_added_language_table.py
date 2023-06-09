"""added Language table

Revision ID: 6630cd25af59
Revises: 
Create Date: 2023-03-30 13:23:03.793914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6630cd25af59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('languages')
    # ### end Alembic commands ###
