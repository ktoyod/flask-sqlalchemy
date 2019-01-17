"""empty message

Revision ID: c05771c82412
Revises: 41ac225740a2
Create Date: 2019-01-09 22:42:19.451802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c05771c82412'
down_revision = '41ac225740a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('article', sa.Text(), nullable=False))
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    op.drop_column('posts', 'article')
    # ### end Alembic commands ###
