import logging
from src.operations.cover_page_operations import update_cover_page
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND

old_file_path = '/src/images/2_Circles.jpg'
new_file_path = '/src/images/camera_hsv.jpg'

operation_status, cover_page = update_cover_page (old_file_path, new_file_path)

if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Updated cover page: {new_file_path} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Cover page: {new_file_path} is not in the database')