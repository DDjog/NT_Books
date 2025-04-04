from sqlalchemy.exc import IntegrityError, OperationalError
import logging

from src.constans import *
from src.database.models import Tag
from src.database.db import session

def add_tag(tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=tag_name).first()

        if not tag:
            tag = Tag(tag=tag_name)
            session.add(tag)
            session.commit()
            logging.info('Tag was added to the database')
            return OPER_ADD_SUCCEEDED, tag.id
        else:
            logging.info('Tag is in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        session.rollback()
        logging.error('No database connection: {e}')
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None

def is_tag_in_db(tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=tag_name).first()

        if tag:
            logging.info('Tag is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, tag.id
        else:
            logging.info('Tag is not in the databse')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_tags_list():
    try:
        tags_list = session.query(Tag).all()

        if tags_list:
            logging.info('Tags list obtained')
            return OPER_GET_LIST_SUCCEEDED, tags_list
        else:
            logging.info('Tags list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_tag(old_tag_name, updated_tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=old_tag_name).first()

        if tag:
            tag.tag = updated_tag_name
            session.commit()
            logging.info('Tag was updated')
            return OPER_UPDATE_SUCCEEDED, tag.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.error(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None


def delete_tag(tag_name):
    try:
        tag = session.query(Tag).filter_by(tag=tag_name).first()

        if tag:
            session.delete(tag)
            session.commit()
            logging.info('Tag was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
             logging.info('Data not found')
             return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION


