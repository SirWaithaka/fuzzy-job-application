"""empty message

Revision ID: 19ec02466227
Revises: a1c18fcb34f5
Create Date: 2017-06-06 20:27:50.407232

"""
from alembic import op
import sqlalchemy as sa
import app
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '19ec02466227'
down_revision = 'a1c18fcb34f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skills')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skills',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('data', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
