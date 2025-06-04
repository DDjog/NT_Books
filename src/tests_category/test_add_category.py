import logging
import src.logging_to_file
from src.operations.category_operations import add_category
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

c = 'Poetry2'
operation_status, category_id = add_category(c)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'Category: {c} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'Category: {c} exists already in the database')