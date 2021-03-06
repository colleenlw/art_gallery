"""empty message

Revision ID: f243ed06451b
Revises: 
Create Date: 2022-05-20 12:09:04.646966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f243ed06451b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('artists',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('artist_firstname', sa.String(length=15), nullable=False),
    sa.Column('artist_lastname', sa.String(length=15), nullable=False),
    sa.Column('artist_location', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=15), nullable=False),
    sa.Column('last_name', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artworks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('date', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=25), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('artwork_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artwork_id'], ['artworks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('art_category',
    sa.Column('artworks_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artworks_id'], ['artworks.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('artworks_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('art_category')
    op.drop_table('categories')
    op.drop_table('customer_accounts')
    op.drop_table('artworks')
    op.drop_table('customers')
    op.drop_table('artists')
    op.drop_table('artist_accounts')
    # ### end Alembic commands ###
