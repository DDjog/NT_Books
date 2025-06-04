import logging
import src.logging_to_file
from src.operations.tag_operations import update_tag
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

t = ['Gmurder', 'murder']
old_tag_name, updated_tag_name = t
operation_status, tag_id = update_tag (old_tag_name, updated_tag_name)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated tag: {updated_tag_name} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Tag: {updated_tag_name} is not in the database')
