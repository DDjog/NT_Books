from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.testing.plugin.plugin_base import logging

from src.database.models import Publisher
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED,\
    OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, \
    OPER_UPDATE_FAILED_DATA_EXISTS



def add_publisher(new_publisher, new_publication_year, new_address_id):
    try:
        publisher = session.query(Publisher).filter_by(publisher=new_publisher, publication_year=new_publication_year, address_id=new_address_id).first()

        if not publisher:
            publisher = Publisher(publisher=new_publisher, publication_year=new_publication_year, address_id=new_address_id)
            session.add(publisher)
            session.commit()
            return OPER_ADD_SUCCEEDED, publisher.id
        else:
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        logging.info(f'Data exists already in the database: {e}')
        session.rollback()
        return OPER_ADD_FAILED_DATA_EXISTS, None

def is_publisher_in_db(publisher, publication_year):
    try:
        publisher = session.query(Publisher).filter_by(publisher=publisher, publication_year=publication_year).first()
        if publisher:
            return OPER_IS_IN_DB_SUCCEEDED, publisher.id
        else:
            return OPER_IS_IN_DB_FAILED, None
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return OPER_IS_IN_DB_FAILED, None

def get_publishers_list():
    try:
        publishers_list = session.query(Publisher).all()
        if publishers_list:
            return OPER_GET_LIST_SUCCEEDED, publishers_list
        else:
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_IS_IN_DB_FAILED

def update_publisher(old_publisher_name, updated_publisher_name, old_publication_year, updated_publication_year):
    try:
        publisher = session.query(Publisher).filter_by(
            publisher=old_publisher_name,
            publication_year=old_publication_year
        ).first()
        if publisher:
            publisher.publisher = updated_publisher_name
            publisher.publication_year = updated_publication_year
            session.commit()
            return OPER_UPDATE_SUCCEEDED, publisher.id
        else:
            return OPER_UPDATE_FAILED_DATA_EXISTS, None
    except IntegrityError as e:
        session.rollback()
        logging.info(f'Data exists already in the database: {e}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

def delete_publisher(publisher_name, publication_year):
    try:
        publisher = session.query(Publisher).filter_by(
            publisher=publisher_name,
            publication_year=publication_year
        ).first()
        if publisher:
            session.delete(publisher)
            session.commit()
            return OPER_DELETE_SUCCEEDED
        else:
            return OPER_DELETE_FAILED_DATA_EXISTS
    except OperationalError as e:
        logging.errror(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_DATA_EXISTS
