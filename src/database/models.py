from sqlalchemy import Column, Integer, String, Table, LargeBinary
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
    isbn = Column(String(13), nullable=True, unique=True)
    cover_page = Column(LargeBinary, nullable=True)
    author = relationship("Author", secondary=book_m2m_author, backref="books")
    tag = relationship("Tag", secondary=book_m2m_tag, backref="books")
    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    publisher = relationship("Publisher", backref="books")
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("BookCategory", backref="books")
    shelf_signature_id = Column(Integer, ForeignKey("shelf_signatures.id"))
    shelf_signature = relationship("BookShelfSignature", backref="books")

class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    language = Column(String(50))


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    author_name = Column(String(50), nullable=True)
    author_surname = Column(String(50), nullable=True)


class Publisher(Base):
    __tablename__ = "publishers"
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
    shelf_code = Column(String(50), nullable=True, unique=False)


