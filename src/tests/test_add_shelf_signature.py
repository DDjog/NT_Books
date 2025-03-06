import logging
import src.logging_to_file
from src.operations.shelf_signature_operations import add_shelf_signature
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS


s = '54678'
operation_status, shelf_signature_id = add_shelf_signature(s)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'Shelf signature: {s} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'Shelf signature: {s} already exists in the database')