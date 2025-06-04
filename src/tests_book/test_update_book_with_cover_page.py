import logging
from src.operations.cover_page_operations import  update_book_with_cover_page
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS, OPER_UPDATE_FAILED_DATA_NOT_FOUND

# from src.tests_cover_page.test_add_cover_page import cover_page_id

book_id = 5
new_cover_page_id= 7
operation_status = update_book_with_cover_page(new_cover_page_id, book_id)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Cover page was added to the book with ID: {book_id}')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND :
    logging.warning(f'Cover page exists already in the database')