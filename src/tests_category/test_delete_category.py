import logging
import src.logging_to_file
from src.operations.category_operations import delete_category
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND

c = 'Poetry'
operation_status = delete_category(c)
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f"{c} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'{c} doesnt exist in the database')