import logging
import src.logging_to_file
from src.operations.shelf_signature_operations import is_shelf_signature_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

a = '523112'
operation_status, shelf_signature_id = is_shelf_signature_in_db(a)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Shelf signature: {a}  is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Shelf signature: {a} is not in the database')