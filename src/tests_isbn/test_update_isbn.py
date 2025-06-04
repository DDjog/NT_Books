import logging
import src.logging_to_file
from src.operations.isbn_operations import update_isbn
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

i = ['G978-1-52943-007-3', 'H978-1-52943-007-3']
old_isbn_number, new_isbn_number = i
operation_status, isbn_id = update_isbn(old_isbn_number, new_isbn_number)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated isbn: {new_isbn_number} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Isbn: {new_isbn_number} is not in the database')