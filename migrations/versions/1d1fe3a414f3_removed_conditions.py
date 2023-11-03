"""Removed conditions

Revision ID: 1d1fe3a414f3
Revises: 3c37a26efb93
Create Date: 2023-11-03 02:44:05.106996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d1fe3a414f3'
down_revision = '3c37a26efb93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)

    # ### end Alembic commands ###
