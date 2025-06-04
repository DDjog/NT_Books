import logging
import src.logging_to_file
from src.operations.cover_page_operations import  delete_cover_page
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND

file_path= '/src/images/2_Circles.jpg'
operation_status = delete_cover_page(file_path)
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f"Cover page was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Cover page doesnt exist in the database')