from sqlalchemy.exc import IntegrityError, OperationalError
from src.database.models import Title
from src.database.db import session
from src.constans import *
import logging


def add_title(title_name):
    try:
        title = session.query(Title).filter_by(title=title_name).first()

        if not title:
            title = Title(title=title_name)
            session.add(title)
            session.commit()
            logging.info('Title was added to the database')
            return OPER_ADD_SUCCEEDED, title.id
        else:
            logging.info('Tag is in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None

def is_title_in_db(title_name):
    try:
        title = session.query(Title).filter_by(title=title_name).first()
        if title:
            logging.info('Title is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, title.id
        else:
            logging.info('Title is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_titles_list():
    try:
        titles_list = session.query(Title).all()
        if titles_list:
            logging.info('Titles list obtained')
            return OPER_GET_LIST_SUCCEEDED, titles_list
        else:
            logging.info('Titles list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_title(old_title_name, updated_title_name):
    try:
        title = session.query(Title).filter_by(title=old_title_name).first()
        if title:
            title.language = updated_title_name
            session.commit()
            logging.info('Title was updated')
            return OPER_UPDATE_SUCCEEDED, title.id
        else:
            logging.info('data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.error(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_title(title_name):
    try:
        title = session.query(Title).filter_by(title=title_name).first()
        if title:
            session.delete(title)
            session.commit()
            logging.info('Title was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION


