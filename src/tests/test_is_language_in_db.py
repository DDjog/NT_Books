import logging
import src.logging_to_file
from src.operations.language_operations import is_language_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

l = 'Spanish'
operation_status, language_id = is_language_in_db (l)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Language: {l} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Language: {l} is not in the database')