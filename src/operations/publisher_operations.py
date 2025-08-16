from sqlalchemy.exc import IntegrityError, OperationalError
import logging

from src.database.models import Publisher
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, \
    OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED, \
    OPER_UPDATE_FAILED_DATA_EXISTS, OPER_ADD_FAILED_NO_DATABASE_CONNECTION, OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, \
    OPER_UPDATE_FAILED_DATA_NOT_FOUND, OPER_UPDATE_FAILED_NO_DB_CONNECTION, OPER_DELETE_FAILED_DATA_NOT_FOUND, \
    OPER_DELETE_FAILED_NO_DB_CONNECTION, OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION


def add_publisher(new_publisher, new_publication_year, new_address_id):
    try:
        publisher = session.query(Publisher).filter_by(publisher=new_publisher, publication_year=new_publication_year, address_id=new_address_id).first()

        if not publisher:
            publisher = Publisher(publisher=new_publisher, publication_year=new_publication_year, address_id=new_address_id)
            session.add(publisher)
            session.commit()
            logging.info('Publisher added to the database')
            return OPER_ADD_SUCCEEDED, publisher.id
        else:
            logging.info('Publisher is in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None

def is_publisher_in_db(publisher, publication_year):
    try:
        publisher = session.query(Publisher).filter_by(publisher=publisher, publication_year=publication_year).first()
        if publisher:
            logging.info('Publisher is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, publisher.id
        else:
            logging.info('Publisher is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_publishers_list():
    try:
        publishers_list = session.query(Publisher).all()
        if publishers_list:
            logging.info('Publishers list obtained')
            return OPER_GET_LIST_SUCCEEDED, publishers_list
        else:
            logging.info('Publishers list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_publisher(old_publisher_name, updated_publisher_name, old_publication_year, updated_publication_year, old_address_id, new_address_idd):
    try:
        publisher = session.query(Publisher).filter_by(
            publisher=old_publisher_name,
            publication_year=old_publication_year,
            address_id = old_address_id
        ).first()
        if publisher:
            publisher.publisher = updated_publisher_name
            publisher.publication_year = updated_publication_year
            session.commit()
            logging.info('Publisher was updated')
            return OPER_UPDATE_SUCCEEDED, publisher.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.error(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_publisher(publisher_name, publication_year):
    try:
        publisher = session.query(Publisher).filter_by(
            publisher=publisher_name,
            publication_year=publication_year
        ).first()
        if publisher:
            session.delete(publisher)
            session.commit()
            logging.info('Publisher was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.errror(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION
