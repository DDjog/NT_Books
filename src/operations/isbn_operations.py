from audioop import error

from sqlalchemy.exc import IntegrityError, OperationalError
import logging

from src.database.models import Isbn
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, \
    OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, \
    OPER_UPDATE_FAILED_DATA_EXISTS, OPER_ADD_FAILED_NO_DATABASE_CONNECTION, OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, \
    OPER_UPDATE_FAILED_DATA_NOT_FOUND, OPER_UPDATE_FAILED_NO_DB_CONNECTION, OPER_DELETE_FAILED_DATA_NOT_FOUND, \
    OPER_DELETE_FAILED_NO_DB_CONNECTION, OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION


def add_isbn(isbn_number):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()

        if not isbn:
            isbn = Isbn(isbn_name=isbn_number)
            session.add(isbn)
            session.commit()
            logging.info('Isbn was added to the database')
            return OPER_ADD_SUCCEEDED, isbn.id
        else:
            logging.info('Isbn exists in the database')
            return  OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        logging.info(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None


def is_isbn_in_db(isbn_number):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()
        if isbn:
            logging.info('Isbn is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, isbn.id
        else:
            logging.info('Isbn is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_isbn_list():
    try:
        isbns_list = session.query(Isbn).all()
        if isbns_list:
            logging.info('Isbns list obtained')
            return OPER_GET_LIST_SUCCEEDED, isbns_list
        else:
            logging.info('Isbns list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_isbn(old_isbn_number, new_isbn_number):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=old_isbn_number).first()
        if isbn:
            isbn.isbn = new_isbn_number
            session.commit()
            logging.info('Isbn was updated')
            return OPER_UPDATE_SUCCEEDED, isbn.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_isbn(isbn_name):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_name).first()
        if isbn:
            session.delete(isbn)
            session.commit()
            logging.info('Isbn was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging,error(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION
