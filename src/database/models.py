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

book_m2m_publisher = Table(
    "book_m2m_publisher",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("publisher_id", Integer, ForeignKey("publishers.id", ondelete="CASCADE")),
                        )

book_m2m_category = Table(
    "book_m2m_category",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("category_id", Integer, ForeignKey("categories.id", ondelete="CASCADE")),
                        )

book_m2m_shelf_signature = Table(
    "book_m2m_shelf_signature",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("shelf_signature_id", Integer, ForeignKey("shelf_signatures.id", ondelete="CASCADE")),
                        )


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    isbn_id = Column(Integer, ForeignKey('isbn.id'), nullable=True, unique=True)
    isbn = relationship('Isbn', backref='books')
    language_id = Column(String(20), nullable=True, unique=True)
    cover_page_id = Column(LargeBinary, ForeignKey('cover_pagr.id'), nullable=True, unique=True)

    language = relationship('Language', backref='books')
    cover_page = relationship('Cover_page', backref='books')
    authors = relationship("Author", secondary=book_m2m_author, backref="books")
    tags = relationship("Tag", secondary=book_m2m_tag, backref="books")
    publisher = relationship('Publisher', secondary=book_m2m_publisher, backref='books')
    category = relationship('Category', secondary=book_m2m_category, backref='books')
    shelf_signature = relationship('Shelf_signature', secondary=book_m2m_shelf_signature, backref='books')


class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    language = Column(String(50))


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    author_name = Column(String(50), nullable=True)
    author_surname = Column(String(50), nullable=True)


class Isbn(Base):
    __tablename__ = "isbn"
    id = Column(Integer, primary_key=True)
    isbn_name = Column(String(50), nullable=True)


class Cover_page(Base):
    __tablename__ = "cover_pages"
    id = Column(Integer, primary_key=True)
    cover_page = Column(LargeBinary(50), nullable=True)


class Publisher(Base):
    __tablename__ = "publisher"
    id = Column(Integer, primary_key=True)
    publisher = Column(String(150), nullable=True, unique=False)
    publication_year = Column(Integer, nullable=True, unique=False)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), nullable=True, unique=False, default=None)


class BookCategory(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=True, unique=False)


class BookShelfSignature(Base):
    __tablename__ = "shelf_signatures"
    id = Column(Integer, primary_key=True)
    shelf_signature = Column(String(50), nullable=True, unique=False)


