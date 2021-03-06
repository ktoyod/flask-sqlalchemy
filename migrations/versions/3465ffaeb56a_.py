"""empty message

Revision ID: 3465ffaeb56a
Revises: 25bd8bada405
Create Date: 2019-03-04 17:07:03.998561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3465ffaeb56a'
down_revision = '25bd8bada405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('authenticated', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    op.drop_column('users', 'authenticated')
    # ### end Alembic commands ###
