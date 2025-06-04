import logging
import src.logging_to_file
from src.operations.cover_page_operations import get_cover_page_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, cover_page_list = get_cover_page_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Cover page list was downloaded from the database:')
    # for index, cover_page in enumerate(cover_page_list, start=1):
        # logging.info(f'{index}. {cover_page.cover_page}')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Cover page list download failed')