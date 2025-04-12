import logging
import src.logging_to_file
from src.operations.category_operations import get_categories_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, categories_list = get_categories_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Categories list was downloaded from the database:')
    for index, category in enumerate(categories_list, start=1):
        logging.info(f'{index}. {category.category_name} ')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Categories list download failed')