import logging
import src.logging_to_file
from src.operations.title_operations import update_title
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

t = ['GHow to solve your own murder', 'How to solve your own murder']
old_title_name, updated_title_name = t
operation_status, title_id = update_title (old_title_name, updated_title_name)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated title: {updated_title_name} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Title: {updated_title_name} is not in the database')
