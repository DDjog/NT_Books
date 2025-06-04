import logging
import src.logging_to_file
from src.operations.author_operations import update_author
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND


a = ['Vincentt', 'AVincentt', 'Severskiii', 'ASeverskiii']
old_author_name, updated_author_name, old_author_surname, updated_author_surname = a
operation_status, author_id = update_author(old_author_name, updated_author_name, old_author_surname, updated_author_surname)

if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Author: {updated_author_name} {updated_author_surname} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Author: {updated_author_name} {updated_author_surname} is not in the database')
