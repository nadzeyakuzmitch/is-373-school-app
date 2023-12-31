"""Changed table name from User to Student

Revision ID: 538e800c4a6d
Revises: 3fa07bb293ee
Create Date: 2023-11-02 23:59:19.184319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '538e800c4a6d'
down_revision = '3fa07bb293ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('student')
    # ### end Alembic commands ###
