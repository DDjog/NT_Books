from audioop import error

from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.testing.plugin.plugin_base import logging

from src.database.models import Isbn
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED,\
    OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, \
    OPER_UPDATE_FAILED_DATA_EXISTS


def add_isbn(isbn_number):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()

        if not isbn:
            isbn = Isbn(isbn_name=isbn_number)
            session.add(isbn)
            session.commit()
            return OPER_ADD_SUCCEEDED, isbn.id
        else:
            return  OPER_ADD_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        logging.info(f'Data exists already in the database: {e}')
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS, None


def is_isbn_in_db(isbn_number):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()
        if isbn:
            return OPER_IS_IN_DB_SUCCEEDED, isbn.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_isbn_list():
    try:
        isbns_list = session.query(Isbn).all()
        if isbns_list:
            return OPER_GET_LIST_SUCCEEDED, isbns_list
        else:
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED

def update_isbn(old_isbn_number, new_isbn_number):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=old_isbn_number).first()
        if isbn:
            isbn.isbn = new_isbn_number
            session.commit()
            return OPER_UPDATE_SUCCEEDED, isbn.id
        else:
            return OPER_UPDATE_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        session.rollback()
        logging.info(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_isbn(isbn_name):
    try:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_name).first()
        if isbn:
            session.delete(isbn)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_DELETE_FAILED_DATA_EXISTS
    except OperationalError as e:
        logging,error(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS
