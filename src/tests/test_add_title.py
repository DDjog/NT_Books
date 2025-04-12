import logging
import src.logging_to_file
from src.operations.title_operations import add_title
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

t = 'Outsider'
operation_status, title_id = add_title(t)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'{t} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'{t} already exists in the database')