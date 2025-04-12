import logging
import src.logging_to_file
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND
from src.operations.address_operations import delete_address


ad = ['Czerska', '8', '10', '00-732', 'Warsaw', 'Poland']
street, number, flat_number, zip_code, city, country = ad
operation_status = delete_address(street, number, flat_number, zip_code, city, country )
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f'Address: {street} {number} {flat_number} {zip_code} {city} {country} was deleted from the database')
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Address: {street} {number} {flat_number} {zip_code} {city} {country} is not in the database')