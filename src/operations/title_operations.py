from sqlalchemy.exc import IntegrityError, OperationalError
from src.database.models import Title
from src.database.db import session
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, \
    OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, OPER_DELETE_FAILED_DATA_EXISTS, OPER_UPDATE_FAILED_DATA_NOT_FOUND, OPER_UPDATE_SUCCEEDED


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
    except IntegrityError:
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
        print(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_titles_list():
    try:
        titles_list = session.query(Title).all()
        if titles_list:
            return OPER_GET_LIST_SUCCEEDED, titles_list
        else:
            return OPER_GET_LIST_FAILED
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED

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
        print(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_title(title_name):
    try:
        title = session.query(Title).filter_by(title=title_name).first()
        if title:
            session.delete(title)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_UPDATE_FAILED_DATA_EXISTS
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS


