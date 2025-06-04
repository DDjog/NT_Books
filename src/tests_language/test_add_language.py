import logging
import src.logging_to_file
from src.operations.language_operations import add_language
from src.constans import  *

l='Fenglish'
operation_status, language_id = add_language(l)

if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'{l} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'{l} already exists in the database')
