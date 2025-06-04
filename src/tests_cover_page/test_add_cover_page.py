import logging
import src.logging_to_file
from src.operations.cover_page_operations import  add_cover_page
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS


file_path= '/Users/dorota/PycharmProjects/NT_Books/src/images/The beautiful mind.jpeg'
operation_status, cover_page_id = add_cover_page(file_path)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'Cover page was added')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'Cover page exists already in the database')