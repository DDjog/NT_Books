from sqlalchemy.exc import IntegrityError, OperationalError
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, \
    OPER_UPDATE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_EXISTS, \
    OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_UPDATE_FAILED_DATA_NOT_FOUND, OPER_UPDATE_SUCCEEDED
from src.database.models import Language
from src.database.db import session

def add_language(language_name):
    try:
        language = session.query(Language).filter_by(language=language_name).first()

        if not language:
            language = Language(language=language_name)
            session.add(language)
            session.commit()
            return OPER_ADD_SUCCEEDED, language.id
        else:
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        print(f'Data exists already in the database: {e}')
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS, None

def is_language_in_db(language_name):
    try:
        language = session.query(Language).filter_by(language=language_name).first()

        if language:
            return OPER_IS_IN_DB_SUCCEEDED, language.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        print(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_languages_list():
    try:
        languages_list = session.query(Language).all()
        if languages_list:
            return OPER_GET_LIST_SUCCEEDED, languages_list
        else:
            return OPER_GET_LIST_FAILED
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED

def update_language(old_language_name, new_language_name):
    try:
        language = session.query(Language).filter_by(language=old_language_name).first()
        if language:
            language.language = new_language_name
            session.commit()
            return OPER_UPDATE_SUCCEEDED, language.id
        else:
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except IntegrityError as e:
        session.rollback()
        print(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_language(language_name):
    try:
        language = session.query(Language).filter_by(language=language_name).first()
        if language:
            session.delete(language)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_DELETE_FAILED_DATA_EXISTS
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS



