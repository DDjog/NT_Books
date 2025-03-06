import logging
import src.logging_to_file
from src.operations.publisher_operations import get_publishers_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED


operation_status, publisher_list = get_publishers_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Publishers list was downloaded from the database:')
    for index, publisher in enumerate(publisher_list, start=1):
        logging.info(f'{index}. {publisher.publisher}, {publisher.publication_year}')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Address list download failed')