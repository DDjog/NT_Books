import logging
import src.logging_to_file
from src.operations.author_operations import is_author_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED


a = ['John', 'Smith']
author_name, author_surname = a
operation_status, author_id = is_author_in_db(author_name, author_surname)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Author: {author_name} {author_surname} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Author: {author_name} {author_surname} is not in the database')