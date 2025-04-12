import logging
import src.logging_to_file
from src.operations.address_operations import update_address
from src.constans import OPER_UPDATE_FAILED_DATA_NOT_FOUND, OPER_UPDATE_SUCCEEDED

a = ['Czerska', 'ACzerska', '8', '18', '10', '11','00-732', '01-731', 'Warsaw', 'AWarsaw', 'Poland', 'APoland']
old_street, updated_street, old_number, updated_number, old_flat_number, updated_flat_number, old_zip_code, updated_zip_code, old_city, updated_city, old_country, updated_country= a
operation_status, address_id = update_address (old_street, updated_street, old_number, updated_number, old_flat_number,
                                               updated_flat_number, old_zip_code, updated_zip_code, old_city, updated_city, old_country, updated_country)

if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated address: {updated_street} {updated_number} {updated_flat_number} {updated_zip_code} {updated_city} {updated_country} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Updated address: {updated_street} {updated_number} {updated_flat_number} {updated_zip_code} {updated_city} {updated_country} is not in the database')
