from sqlalchemy.exc import IntegrityError, OperationalError
import logging

from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, \
    OPER_UPDATE_SUCCEEDED, OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_EXISTS, OPER_IS_IN_DB_SUCCEEDED, \
    OPER_IS_IN_DB_FAILED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_UPDATE_FAILED_DATA_NOT_FOUND, \
    OPER_ADD_FAILED_NO_DATABASE_CONNECTION, OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, OPER_UPDATE_FAILED_NO_DB_CONNECTION, \
    OPER_DELETE_FAILED_DATA_NOT_FOUND, OPER_DELETE_FAILED_NO_DB_CONNECTION, OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION
from src.database.models import Category
from src.database.db import session

def add_category(category_name):
    try:
        category = session.query(Category).filter_by(category_name=category_name).first()
        if not category:
            category = Category(category_name=category_name)
            session.add(category)
            session.commit()
            logging.info('Category was added in the database')
            return OPER_ADD_SUCCEEDED, category.id
        else:
            logging.info('Category exists in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION,None

def is_category_in_db(category_name):
    try:
        category = session.query(Category).filter_by(category_name=category_name).first()
        if category:
            logging.info('Category is  in the database')
            return OPER_IS_IN_DB_SUCCEEDED, category.id
        else:
            logging.info('Category is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_categories_list():
    try:
        categories_list = session.query(Category).all()
        if categories_list:
            logging.info('Categories list got')
            return OPER_GET_LIST_SUCCEEDED, categories_list
        else:
            logging.info('Categories list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_category(old_category_name, updated_category_name):
    try:
        category = session.query(Category).filter_by(category_name=old_category_name).first()
        if category:
            category.category_name = updated_category_name
            session.commit()
            logging.info('Category was updated')
            return OPER_UPDATE_SUCCEEDED, category.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_category(category_name):
    try:
        category = session.query(Category).filter_by(category_name=category_name).first()
        if category:
            session.delete(category)
            session.commit()
            logging.info('Category was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION


