import logging
import src.logging_to_file
from src.operations.books_operations import get_books_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, books_list = get_books_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Books list was downloaded from the database:')
    for index, book in enumerate(books_list, start=1):
        logging.info(f'{index}. {book.title.title}, {book.isbn.isbn_name}')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Books list download failed')