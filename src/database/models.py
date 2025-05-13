from enum import unique
from unicodedata import category

from sqlalchemy import Column, Integer, String, Table, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base() 

book_m2m_author = Table(
    "book_m2m_author",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("author_id", Integer, ForeignKey("authors.id", ondelete="CASCADE")),
                        )

book_m2m_tag = Table(
    "book_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
                        )

# book_m2m_publisher = Table(
#     "book_m2m_publisher",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
#     Column("publisher_id", Integer, ForeignKey("publishers.id", ondelete="CASCADE")),
#                         )

book_m2m_category = Table(
    "book_m2m_category",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("category_id", Integer, ForeignKey("categories.id", ondelete="CASCADE")),
                        )

# book_m2o_shelf_signature = Table(
#     "book_m2o_shelf_signature",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
#     Column("shelf_signature_id", Integer, ForeignKey("shelf_signatures.id", ondelete="CASCADE")),
#                         )

# book_m2m_cover_page = Table(
#     "book_m2m_cover_page",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
#     Column("cover_page_id", Integer, ForeignKey("cover_page.id", ondelete="CASCADE")),
#                         )

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('titles.id'), nullable=True, unique=True)
    isbn_id = Column(Integer, ForeignKey('isbn.id'), nullable=True, unique=True)
    language_id = Column(Integer, ForeignKey('languages.id'), nullable=True)
    # cover_page_id = Column(LargeBinary, ForeignKey('cover_pages.id'), nullable=True, unique=True)
    shelf_signature_id = Column(Integer, ForeignKey('shelf_signatures.id'), nullable=True)
    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable=True)

    title = relationship('Title', backref='books')
    isbn = relationship('Isbn', backref='books')
    language = relationship('Language', backref='books')
    # cover_page = relationship('Cover_page', backref='books')
    authors = relationship("Author", secondary=book_m2m_author, backref="books")
    tags = relationship("Tag", secondary=book_m2m_tag, backref="books")
    publisher = relationship('Publisher', backref='books')
    categories = relationship('Category', secondary=book_m2m_category, backref='books')
    shelf_signature = relationship('ShelfSignature', backref='books')

class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    language = Column(String(50))

class Title(Base):
    __tablename__ = "titles"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True, unique=True)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    author_name = Column(String(50), nullable=True)
    author_surname = Column(String(50), nullable=True)

class Isbn(Base):
    __tablename__ = "isbn"
    id = Column(Integer, primary_key=True)
    isbn_name = Column(String(50), nullable=True, unique=True)


class Cover_page(Base):
    __tablename__ = "cover_pages"
    id = Column(Integer, primary_key=True)
    cover_page = Column(LargeBinary, nullable=True)

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    street = Column(String(100), nullable=False)
    number = Column(String(50), nullable=False, unique=False)
    flat_number = Column(String(50), nullable=True, unique=False)
    zip_code = Column(String(50), nullable=False, unique=False)
    city = Column(String(100), nullable=False, unique=False)
    country = Column(String(80), nullable=False, unique=False)


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True)
    publisher = Column(String(150), nullable=True, unique=False)
    publication_year = Column(Integer, nullable=True, unique=False)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), nullable=True, unique=False, default=None)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=True, unique=False)


class ShelfSignature(Base):
    __tablename__ = "shelf_signatures"
    id = Column(Integer, primary_key=True)
    shelf_signature = Column(String(50), nullable=True, unique=False)


