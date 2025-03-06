from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.testing.plugin.plugin_base import logging

from src.database.models import ShelfSignature
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, \
    OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_UPDATE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, OPER_IS_IN_DB_FAILED, OPER_IS_IN_DB_SUCCEEDED


def add_shelf_signature(shelf_signature_number):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

        if not shelf_signature:
            shelf_signature = ShelfSignature(shelf_signature=shelf_signature_number)
            session.add(shelf_signature)
            session.commit()
            return OPER_ADD_SUCCEEDED, shelf_signature.id
        else:
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        logging.info(f'Data exists already in the database: {e}')
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS,None


def is_shelf_signature_in_db(shelf_signature_number):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

        if shelf_signature:
            return OPER_IS_IN_DB_SUCCEEDED, shelf_signature.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_shelf_signatures_list():
    try:
        shelf_signatures_list = session.query(ShelfSignature).all()
        if shelf_signatures_list:
            return OPER_GET_LIST_SUCCEEDED, shelf_signatures_list
        else:
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_GET_LIST_FAILED

def update_shelf_signature(old_shelf_signature, new_shelf_signature):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=old_shelf_signature).first()

        if shelf_signature:
            shelf_signature.shelf_signature = new_shelf_signature
            session.commit()
            return OPER_UPDATE_SUCCEEDED, shelf_signature.id
        else:
            return OPER_UPDATE_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        session.rollback()
        logging.info(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_shelf_signature(shelf_signature_number):
    try:
        shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

        if shelf_signature:
            session.delete(shelf_signature)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_DELETE_FAILED_DATA_EXISTS
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS