import logging
import src.logging_to_file
from src.operations.address_operations import add_address
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

ad = ['Czerska', '8', '10', '00-732', 'Warsaw', 'Poland']
street, number, flat_number, zip_code, city, country = ad
operation_status, address_id = add_address(street, number, flat_number, zip_code, city, country)

if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f"Address: {street} {number} {flat_number} {zip_code} {city} {country} was added to the database")
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f"Address: {street} {number} {flat_number} {zip_code} {city} {country} is already in the database")
