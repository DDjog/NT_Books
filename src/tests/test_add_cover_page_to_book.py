import logging
import src.logging_to_file
from src.operations.cover_page_operations import  add_cover_page
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

i = (1,'src/images/2_Circles.jpg')
operation_status, book_id = add_cover_page(i)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'Image was added to the book with ID: {book_id}')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'Image: {i} exists already in the database')