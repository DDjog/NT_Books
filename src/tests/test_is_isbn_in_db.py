import logging
import src.logging_to_file
from src.operations.isbn_operations import is_isbn_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

isn = '978-3-16-148410-0'
operation_status, isbn_id = is_isbn_in_db (isn)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Isbn:{isn} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Isbn: {isn} is not in the database')