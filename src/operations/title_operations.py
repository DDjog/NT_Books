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
            return OPER_ADD_SUCCEEDED, title.id
        else:
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        logging.info(f'Data exists already in the database: {e}')
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS, None

def is_title_in_db(title_name):
    try:
        title = session.query(Title).filter_by(title=title_name).first()
        if title:
            return OPER_IS_IN_DB_SUCCEEDED, title.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_titles_list():
    try:
        titles_list = session.query(Title).all()
        if titles_list:
            return OPER_GET_LIST_SUCCEEDED, titles_list
        else:
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED, None

def update_title(old_title_name, updated_title_name):
    try:
        title = session.query(Title).filter_by(title=old_title_name).first()
        if title:
            title.language = updated_title_name
            session.commit()
            return OPER_UPDATE_SUCCEEDED, title.id
        else:
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except IntegrityError as e:
        session.rollback()
        logging.info(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_title(title_name):
    try:
        title = session.query(Title).filter_by(title=title_name).first()
        if title:
            session.delete(title)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS


