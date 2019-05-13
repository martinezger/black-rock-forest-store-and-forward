"""add is_collected

Revision ID: c7698f6db48a
Revises: ad970d351fc3
Create Date: 2019-05-12 19:20:27.325141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7698f6db48a'
down_revision = 'ad970d351fc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sensordata', sa.Column('is_collected', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensordata', 'is_collected')
    # ### end Alembic commands ###