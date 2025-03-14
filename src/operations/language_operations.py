from sqlalchemy.exc import IntegrityError, OperationalError
import logging

from src.constans import *
from src.database.models import Language
from src.database.db import session

def add_language(language_name):
    try:
        language = session.query(Language).filter_by(language=language_name).first()

        if not language:
            language = Language(language=language_name)
            session.add(language)
            session.commit()
            logging.info('Language was added to the database')
            return OPER_ADD_SUCCEEDED, language.id
        else:
            logging.info('Language is in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        logging.info(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None

def is_language_in_db(language_name):
    try:
        language = session.query(Language).filter_by(language=language_name).first()

        if language:
            logging.info('Language was added to the database')
            return OPER_IS_IN_DB_SUCCEEDED, language.id
        else:
            logging.info('Language is in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_languages_list():
    try:
        languages_list = session.query(Language).all()
        if languages_list:
            logging.info('Languages list obtained')
            return OPER_GET_LIST_SUCCEEDED, languages_list
        else:
            logging.info('Languages list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_language(old_language_name, new_language_name):
    try:
        language = session.query(Language).filter_by(language=old_language_name).first()
        if language:
            language.language = new_language_name
            session.commit()
            logging.info('Language was updated')
            return OPER_UPDATE_SUCCEEDED, language.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_language(language_name):
    try:
        language = session.query(Language).filter_by(language=language_name).first()
        if language:
            session.delete(language)
            session.commit()
            logging.info('Language was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION



