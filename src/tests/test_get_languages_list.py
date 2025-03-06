import logging
import src.logging_to_file
from src.operations.language_operations import get_languages_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, languages_list = get_languages_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Languages list was downloaded from the database:')
    for index, language in enumerate(languages_list, start=1):
        logging.info(f'{index}. {language.language} ')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Languages list download failed')