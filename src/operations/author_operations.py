import logging

from sqlalchemy.exc import IntegrityError, OperationalError
from src.constans import *
from src.database.models import Author, Book, Title, Isbn
from src.database.db import session



def add_author(new_author_name, new_author_surname):
    try:
        author = session.query(Author).filter_by(
            author_name=new_author_name,
            author_surname=new_author_surname
        ).first()

        if not author:
            author = Author(author_name=new_author_name,
                            author_surname=new_author_surname)
            session.add(author)
            session.commit()
            return OPER_ADD_SUCCEEDED, author.id
        else:
            return  OPER_ADD_FAILED_DATA_EXISTS, None

    except IntegrityError as e:
        logging.info(f'Data exists already in the database: {e}')
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS, None


def add_author_to_the_book(title, isbn, ad_author_name, ad_author_surname):
    try:
        book = session.query(Book).join(Title).join(Isbn).filter(
            Title.title == title,
            Isbn.isbn_name == isbn
        ).first()
        if not book:
            return OPER_ADD_FAILED_DATA_EXISTS, None

        author = session.query(Author).filter_by(
            author_name=ad_author_name,
            author_surname=ad_author_surname
        ).first()

        if not author:
            author = Author(
                author_name=ad_author_name,
                author_surname=ad_author_surname)
            session.add(author)
            session.commit()

        if author not in book.authors:
            book.authors.append(author)
            session.commit()
            return OPER_ADD_SUCCEEDED, author.id
        else:
            return  OPER_ADD_FAILED_DATA_EXISTS, None
    except Exception as e:
        session.rollback()
        logging.error(f'Unexpected error: {e}')


def is_author_in_db(author_name, author_surname):
    try:
        author = session.query(Author).filter_by(
            author_name=author_name,
            author_surname=author_surname
        ).first()
        if author:
            return OPER_IS_IN_DB_SUCCEEDED, author.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None


def get_authors_list():
    try:
        authors_list = session.query(Author).all()
        if authors_list:
            return OPER_GET_LIST_SUCCEEDED, authors_list
        else:
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED

def update_author(old_author_name, updated_author_name,  old_author_surname, updated_author_surname):
    try:
        author = session.query(Author).filter(
            Author.author_name==old_author_name,
            Author.author_surname==old_author_surname
        ).first()
        if author:
            author.author_name = updated_author_name
            author.author_surname = updated_author_surname
            session.commit()
            return OPER_UPDATE_SUCCEEDED, author.id
        else:
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except IntegrityError as e:
        session.rollback()
        print(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_author(author_name, author_surname):
    try:
        author = session.query(Author).filter_by(
            author_name=author_name,
            author_surname=author_surname
        ).first()
        if author:
            session.delete(author)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_DELETE_FAILED_DATA_EXISTS
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS



