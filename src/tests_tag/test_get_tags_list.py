import logging
import src.logging_to_file
from src.operations.tag_operations import get_tags_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, tags_list = get_tags_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Tags list was downloaded from the database:')
    for index, tag in enumerate(tags_list, start=1):
        logging.info(f'{index}. {tag.tag}')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Tags list download failed')