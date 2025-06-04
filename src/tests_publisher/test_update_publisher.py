import logging
import src.logging_to_file
from src.operations.publisher_operations import update_publisher
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

s = ['FQuercus', 'GQuercus', 4212024, 1975]
old_publisher_name, updated_publisher_name, old_publication_year, updated_publication_year = s
operation_status, publisher_id = update_publisher(old_publisher_name, updated_publisher_name, old_publication_year, updated_publication_year)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated publisher: {updated_publisher_name} with publication year {updated_publication_year} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Publisher: {updated_publisher_name} with publication year {updated_publication_year} is not in the database')