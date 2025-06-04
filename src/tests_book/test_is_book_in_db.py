import logging
import src.logging_to_file
from src.operations.books_operations import is_book_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

a = ['GHow to solve your own murder', 'G978-1-52943-007-3']
title, isbn = a
operation_status, book_id = is_book_in_db(title, isbn)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Book: {title} with isbn: {isbn} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Book: {title} with isbn: {isbn} is not in the database')