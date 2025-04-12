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
            logging.info('Author added to the database')
            return OPER_ADD_SUCCEEDED, author.id
        else:
            logging.info('Author already exists in the database')
            return  OPER_ADD_FAILED_DATA_EXISTS, None

    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None


def add_author_to_the_book(title, isbn, ad_author_name, ad_author_surname):
    try:
        book = session.query(Book).join(Title).join(Isbn).filter(
            Title.title == title,
            Isbn.isbn_name == isbn
        ).first()
        if book is None:
            logging.info('No book in the database')
            return OPER_ADD_FAILED_DATA_NOT_IN_DB, None

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
            logging.info('Author added to the database')
        else:
            logging.info('Author is already in the database')

        if author not in book.authors:
            book.authors.append(author)
            session.commit()
            logging.info('Additional author was added to the book')
            return OPER_ADD_SUCCEEDED, author.id
        else:
            logging.info('Author is already added to the book')
            return  OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        session.rollback()
        logging.error(f'No database connection: {e}')


def is_author_in_db(author_name, author_surname):
    try:
        author = session.query(Author).filter_by(
            author_name=author_name,
            author_surname=author_surname
        ).first()
        if author:
            logging.info('Author is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, author.id
        else:
            logging.info('Author is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None


def get_authors_list():
    try:
        authors_list = session.query(Author).all()
        if authors_list:
            logging.info('Authors list got')
            return OPER_GET_LIST_SUCCEEDED, authors_list
        else:
            logging.info('Authors list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

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
            logging.info('Author was updated')
            return OPER_UPDATE_SUCCEEDED, author.id
        else:
            logging.info('Author not in the database')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.error(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_author(author_name, author_surname):
    try:
        author = session.query(Author).filter_by(
            author_name=author_name,
            author_surname=author_surname
        ).first()
        if author:
            session.delete(author)
            session.commit()
            logging.info('Author deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Author not found in the database')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION



