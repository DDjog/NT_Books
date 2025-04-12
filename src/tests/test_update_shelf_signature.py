import logging
import src.logging_to_file
from src.operations.shelf_signature_operations import update_shelf_signature
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

s = ['523112', '623112']
old_shelf_signature, new_shelf_signature = s
operation_status, shelf_signature_id = update_shelf_signature(old_shelf_signature, new_shelf_signature)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated shelf signature: {new_shelf_signature} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Shelf signature: {new_shelf_signature} is not in the database')
