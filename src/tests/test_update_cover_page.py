import logging
import src.logging_to_file
from src.operations.cover_page_operations import update_cover_page
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

old_file_path = '/Users/dorota/PycharmProjects/NT_Books/src/images/2_Circles.jpg'
new_file_path = '/Users/dorota/PycharmProjects/NT_Books/src/images/alien1.jpg'
operation_status, cover_page = update_cover_page (old_file_path, new_file_path)
if operation_status == OPER_UPDATE_SUCCEEDED:
    None
    # logging.info(f'Updated cover page: {new_file_path} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    # logging.warning(f'Cover page: {new_file_path} is not in the database')
    None