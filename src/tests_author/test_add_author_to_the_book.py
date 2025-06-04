import logging
import src.logging_to_file
from src.operations.author_operations import add_author_to_the_book
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

ad_au = ['GHow to solve your own murder', 'G978-1-52943-007-3', 'Al', 'Rumsky']
title, isbn, ad_author_name, ad_author_surname = ad_au
operation_status, author_id = add_author_to_the_book(title, isbn, ad_author_name, ad_author_surname)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'Author: {ad_author_name} {ad_author_surname} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    logging.warning(f'Author: {ad_author_name} {ad_author_surname} is already in the database')