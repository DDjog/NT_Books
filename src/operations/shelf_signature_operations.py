from sqlalchemy.exc import IntegrityError, OperationalError
import logging

from src.database.models import ShelfSignature
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, \
    OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_UPDATE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, OPER_IS_IN_DB_FAILED, OPER_IS_IN_DB_SUCCEEDED, \
    OPER_ADD_FAILED_NO_DATABASE_CONNECTION, OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, \
    OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, OPER_UPDATE_FAILED_DATA_NOT_FOUND, OPER_UPDATE_FAILED_NO_DB_CONNECTION, \
    OPER_DELETE_FAILED_DATA_NOT_FOUND, OPER_DELETE_FAILED_NO_DB_CONNECTION


def add_shelf_signature(shelf_signature_number):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

        if not shelf_signature:
            shelf_signature = ShelfSignature(shelf_signature=shelf_signature_number)
            session.add(shelf_signature)
            session.commit()
            logging.info('Shelf signature was added')
            return OPER_ADD_SUCCEEDED, shelf_signature.id
        else:
            logging.info('Shelf signature is in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION,None


def is_shelf_signature_in_db(shelf_signature_number):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

        if shelf_signature:
            logging.info('Shelf signature is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, shelf_signature.id
        else:
            logging.info('Shelf signature is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_shelf_signatures_list():
    try:
        shelf_signatures_list = session.query(ShelfSignature).all()
        if shelf_signatures_list:
            logging.info('Shelf signatures list obtained')
            return OPER_GET_LIST_SUCCEEDED, shelf_signatures_list
        else:
            logging.info('Shelf signatures list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_shelf_signature(old_shelf_signature, new_shelf_signature):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=old_shelf_signature).first()

        if shelf_signature:
            shelf_signature.shelf_signature = new_shelf_signature
            session.commit()
            logging.info('Shelf signature was updated')
            return OPER_UPDATE_SUCCEEDED, shelf_signature.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_shelf_signature(shelf_signature_number):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

        if shelf_signature:
            session.delete(shelf_signature)
            session.commit()
            logging.info('Shelf signature was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION