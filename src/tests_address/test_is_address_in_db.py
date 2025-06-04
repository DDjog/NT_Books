import logging
import src.logging_to_file
from src.operations.address_operations import is_address_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

a = ['Czerska', '8', '10', '00-732', 'Warsaw', 'Poland']
street, number, flat_number, zip_code, city, country = a
operation_status, address_id = is_address_in_db(street, number, number, flat_number, city, country)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Address: {street} {number} {flat_number} {zip_code} {city} {country} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Address: {street} {number} {flat_number} {zip_code} {city} {country} is not in the database')