import logging

from sqlalchemy.exc import IntegrityError, OperationalError

from src.database.models import Address
from src.database.db import session
from src.constans import *


def add_address(new_street, new_number, new_flat_number, new_zip_code,
                new_city, new_country):
    try:
        address = session.query(Address).filter_by(
            street=new_street,
            number= new_number,
            flat_number= new_flat_number,
            zip_code=new_zip_code,
            city=new_city,
            country=new_country
        ).first()

        if not address:
            address = Address(
                street=new_street,
                number=new_number,
                flat_number=new_flat_number,
                zip_code=new_zip_code,
                city=new_city,
                country=new_country
            )
            session.add(address)
            session.commit()
            logging.info('Address addded to the database')
            return OPER_ADD_SUCCEEDED, address.id
        else:
            logging.info('Address exists already in the database')
            return OPER_ADD_FAILED_DATA_NOT_IN_DB, None


    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None


def is_address_in_db(street, number, flat_number, zip_code,city, country):
    try:
        address = session.query(Address).filter_by(
            street=street,
            number=number,
            flat_number=flat_number,
            zip_code=zip_code,
            city=city,
            country=country
        ).first()

        if address:
            logging.info('Address exists in the database')
            return OPER_IS_IN_DB_SUCCEEDED, address.id
        else:
            logging.info('Address is not in the database')
            return OPER_IS_IN_DB_FAILED, None

    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None

def get_addresses_list():
    try:
        addresses_list = session.query(Address).all()
        if addresses_list:
            logging.info('Address list got')
            return OPER_GET_LIST_SUCCEEDED, addresses_list
        else:
            logging.info('Address list failed')
            return OPER_GET_LIST_FAILED, None

    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_address(old_street, updated_street, old_number, updated_number, old_flat_number, updated_number_flat,
                    old_zip_code, updated_zip_code, old_city, updated_city, old_country, updated_country):
    try:
        address = session.query(Address).filter(
            Address.street==old_street,
            Address.number==old_number,
            Address.flat_number==old_flat_number,
            Address.zip_code==old_zip_code,
            Address.city==old_city,
            Address.country==old_country
        ).first()

        if address:
            address.street=updated_street
            address.number=updated_number
            address.flat_number=updated_number_flat
            address.zip_code=updated_zip_code
            address.city=updated_city
            address.country=updated_country

            session.commit()
            logging.info('Address updated')
            return OPER_UPDATE_SUCCEEDED, address.id
        else:
            logging.info('Address is already in the database')
            return OPER_UPDATE_FAILED_DATA_EXISTS, None
    except OperationalError as e:
        session.rollback()
        logging.error(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_address(street, number, flat_number,zip_code, city, country):
    try:
        address = session.query(Address).filter_by(
            street=street,
            number=number,
            flat_number=flat_number,
            zip_code=zip_code,
            city=city,
            country=country
        ).first()
        if address:
            session.delete(address)
            session.commit()
            logging.info('Address deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION

