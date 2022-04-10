"""empty message

Revision ID: 564e5c010524
Revises: 
Create Date: 2022-04-10 16:49:39.448835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '564e5c010524'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_item_item_id'), 'user_item', ['item_id'], unique=False)
    op.create_index(op.f('ix_user_item_user_id'), 'user_item', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_item_user_id'), table_name='user_item')
    op.drop_index(op.f('ix_user_item_item_id'), table_name='user_item')
    op.drop_table('user_item')
    # ### end Alembic commands ###
