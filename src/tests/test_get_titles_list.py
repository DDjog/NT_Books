import logging
import src.logging_to_file
from src.operations.title_operations import get_titles_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, titles_list = get_titles_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Titles list was downloaded from the database:')
    for index, title in enumerate(titles_list, start=1):
        logging.info(f'{index}. {title.title} ')
elif operation_status== OPER_GET_LIST_FAILED:
    logging.warning('Titles list download failed')