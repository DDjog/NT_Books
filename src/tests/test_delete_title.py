import logging
import src.logging_to_file
from src.operations.title_operations import delete_title
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND


t = 'Outsiders'
operation_status = delete_title(t)
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f"Title: {t} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Title: {t} doesnt exist in the database')