import logging
import src.logging_to_file
from src.operations.author_operations import get_authors_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED


operation_status, authors_list = get_authors_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Authors list was downloaded from the database:')
    for index, author in enumerate(authors_list, start=1):
        logging.info(f'{index}. {author.author_name}, {author.author_surname}')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Authors list download failed')