"""empty message

Revision ID: 198072ade5f6
Revises: e2f3bfd1f998
Create Date: 2019-12-16 20:26:35.013101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198072ade5f6'
down_revision = 'e2f3bfd1f998'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('questions', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member', 'questions')
    # ### end Alembic commands ###
