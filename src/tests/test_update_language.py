import logging
import src.logging_to_file
from src.operations.language_operations import update_language
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

l = ['Genglish', 'English']
old_language_name, new_language_name = l
operation_status, language_id = update_language (old_language_name, new_language_name)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated language: {new_language_name} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Language: {new_language_name} is not in the database')
