from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
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

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    isbn = Column(Integer, nullable=True, unique=True)
    cover_page = Column(String, nullable=True)
    author = relationship("Author", backref="authors")
    tag = relationship("Tag", backref="books")

class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    language = Column(String(50))

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    author_name = Column(String(50), nullable=True)
    author_surname = Column(String(50), nullable=True)

class Publisher(Base):
    __tablename__ = "publisher"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    publisher = Column(String(150), nullable=True, unique=False)
    publication_year = Column(Integer, nullable=True, unique=False)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    tag = Column(String(50), nullable=True, unique=False, default=None)

class BookCathegory(Base):
    __tablename__ = "cathegories"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    name = Column(String(50), nullable=True, unique=False)

class BookLocalisation(Base):
    __tablename__ = "localisations"
    id = Column(Integer, primary_key=True)
    cathegory_id = Column(Integer, ForeignKey("cathegories.id", ondelete="CASCADE"))
    publisher = Column(String(150), nullable=True, unique=False)
    bookshelf_no = Column(Integer, nullable=True, unique=False)


