import logging
import src.logging_to_file
from src.operations.isbn_operations import delete_isbn
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND

i = '765-88-54-00000-1'
operation_status = delete_isbn(i)
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f"{i} was deleted to the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'{i} exists not in the database')