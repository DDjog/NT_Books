import logging
import src.logging_to_file
from src.operations.isbn_operations import add_isbn
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

i = '765-88-54-00000-1'
operation_status, isbn_id = add_isbn(i)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f"Isbn: {i} was added to the database")
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'Isbn:{i} exists already in the database')