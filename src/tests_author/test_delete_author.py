import logging
import src.logging_to_file
from src.operations.author_operations import delete_author
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND

a = ['Vincentt', 'Severskiii']
author_name, author_surname = a
operation_status = delete_author(author_name, author_surname)
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f'Author:{a} was deleted from the database')
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Author: {a} exists not in the database')