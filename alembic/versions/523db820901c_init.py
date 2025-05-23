"""Init

Revision ID: 523db820901c
Revises: 
Create Date: 2025-05-13 20:50:49.757360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '523db820901c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=100), nullable=False),
    sa.Column('number', sa.String(length=50), nullable=False),
    sa.Column('flat_number', sa.String(length=50), nullable=True),
    sa.Column('zip_code', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_name', sa.String(length=50), nullable=True),
    sa.Column('author_surname', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cover_pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cover_page', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('isbn',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isbn_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn_name')
    )
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shelf_signatures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shelf_signature', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('publishers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('publisher', sa.String(length=150), nullable=True),
    sa.Column('publication_year', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_id', sa.Integer(), nullable=True),
    sa.Column('isbn_id', sa.Integer(), nullable=True),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('cover_page_id', sa.Integer(), nullable=True),
    sa.Column('shelf_signature_id', sa.Integer(), nullable=True),
    sa.Column('publisher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cover_page_id'], ['cover_pages.id'], ),
    sa.ForeignKeyConstraint(['isbn_id'], ['isbn.id'], ),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], ),
    sa.ForeignKeyConstraint(['publisher_id'], ['publishers.id'], ),
    sa.ForeignKeyConstraint(['shelf_signature_id'], ['shelf_signatures.id'], ),
    sa.ForeignKeyConstraint(['title_id'], ['titles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cover_page_id'),
    sa.UniqueConstraint('isbn_id'),
    sa.UniqueConstraint('title_id')
    )
    op.create_table('book_m2m_author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_m2m_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_m2m_cover_page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('cover_page_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['cover_page_id'], ['cover_pages.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_m2m_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_m2m_tag')
    op.drop_table('book_m2m_cover_page')
    op.drop_table('book_m2m_category')
    op.drop_table('book_m2m_author')
    op.drop_table('books')
    op.drop_table('publishers')
    op.drop_table('titles')
    op.drop_table('tags')
    op.drop_table('shelf_signatures')
    op.drop_table('languages')
    op.drop_table('isbn')
    op.drop_table('cover_pages')
    op.drop_table('categories')
    op.drop_table('authors')
    op.drop_table('addresses')
    # ### end Alembic commands ###
