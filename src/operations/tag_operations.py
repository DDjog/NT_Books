from sqlalchemy.exc import IntegrityError, OperationalError
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, \
    OPER_UPDATE_FAILED_DATA_EXISTS, OPER_UPDATE_SUCCEEDED, OPER_DELETE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, OPER_UPDATE_FAILED_DATA_NOT_FOUND
from src.database.models import Tag
from src.database.db import session

def add_tag(tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=tag_name).first()

        if not tag:
            tag = Tag(tag=tag_name)
            session.add(tag)
            session.commit()
            return OPER_ADD_SUCCEEDED, tag.id
        else:
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except IntegrityError:
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS, None

def is_tag_in_db(tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=tag_name).first()

        if tag:
            return OPER_IS_IN_DB_SUCCEEDED, tag.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        print(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_tags_list():
    try:
        tags_list = session.query(Tag).all()

        if tags_list:
            return OPER_GET_LIST_SUCCEEDED, tags_list
        else:
            return OPER_GET_LIST_FAILED
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED

def update_tag(old_tag_name, updated_tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=old_tag_name).first()

        if tag:
            tag.tag = updated_tag_name
            session.commit()
            return OPER_UPDATE_SUCCEEDED, tag.id
        else:
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except IntegrityError as e:
        session.rollback()
        print(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None


def delete_tag(tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=tag_name).first()

        if tag:
            session.delete(tag)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
             return OPER_DELETE_FAILED_DATA_EXISTS
    except OperationalError as e:
        print(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS


