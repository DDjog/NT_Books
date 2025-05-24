import logging
import src.logging_to_file
from src.operations.cover_page_operations import  update_book_with_cover_page
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_NO_DB_CONNECTION, OPER_UPDATE_FAILED_DATA_EXISTS
from src.tests.test_add_cover_page_to_book import cover_page_id

book_id = 1
new_cover_page_id= 2
operation_status = update_book_with_cover_page(new_cover_page_id, book_id)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Cover page with ID: {cover_page_id} was added to the book with ID: {book_id}')
elif operation_status == OPER_UPDATE_FAILED_DATA_EXISTS :
    logging.warning(f'Cover page exists already in the database')