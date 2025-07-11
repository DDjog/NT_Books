"""Add book_id to cover_pages

Revision ID: e85537250102
Revises: 523db820901c
Create Date: 2025-05-29 21:17:34.440732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e85537250102'
down_revision: Union[str, None] = '523db820901c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_m2m_cover_page')
    op.drop_constraint('books_cover_page_id_key', 'books', type_='unique')
    op.drop_constraint('books_cover_page_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'cover_page_id')
    op.add_column('cover_pages', sa.Column('book_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cover_pages', 'books', ['book_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cover_pages', type_='foreignkey')
    op.drop_column('cover_pages', 'book_id')
    op.add_column('books', sa.Column('cover_page_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('books_cover_page_id_fkey', 'books', 'cover_pages', ['cover_page_id'], ['id'])
    op.create_unique_constraint('books_cover_page_id_key', 'books', ['cover_page_id'])
    op.create_table('book_m2m_cover_page',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cover_page_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='book_m2m_cover_page_book_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['cover_page_id'], ['cover_pages.id'], name='book_m2m_cover_page_cover_page_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='book_m2m_cover_page_pkey')
    )
    # ### end Alembic commands ###
