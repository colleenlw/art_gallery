"""empty message

Revision ID: 23c3fa4693aa
Revises: f243ed06451b
Create Date: 2022-05-20 12:11:32.739996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23c3fa4693aa'
down_revision = 'f243ed06451b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist_accounts', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'artist_accounts', 'artists', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'artist_accounts', type_='foreignkey')
    op.drop_column('artist_accounts', 'artist_id')
    # ### end Alembic commands ###
