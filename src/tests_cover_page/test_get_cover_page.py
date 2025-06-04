import logging
import src.logging_to_file
from src.operations.cover_page_operations import get_cover_page, get_cover_page_list
from src.constans import OPER_GET_SUCCEEDED, OPER_GET_FAILED_NO_DATA


cover_page_id = 2
output_path = '/downloads/2_Circles.jpg'

operation_status, file_path = get_cover_page(cover_page_id, output_path)
if operation_status == OPER_GET_SUCCEEDED:
    logging.info(f'Cover page saved to {output_path}')
elif operation_status == OPER_GET_FAILED_NO_DATA:
    logging.warning('Cover page failed to be saved')

