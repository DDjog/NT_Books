import logging
import src.logging_to_file
from src.operations.tag_operations import add_tag
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

t = 'New Year'
operation_status, tag_id = add_tag(t)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'{t} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'{t} already exists in the database')