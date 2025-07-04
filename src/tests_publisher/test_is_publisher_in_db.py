import logging
from src.operations.publisher_operations import is_publisher_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

p = ['AXA', 2009]
publisher, publication_year = p
operation_status, publisher_id = is_publisher_in_db (publisher, publication_year)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    logging.info(f'Publisher: {p} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    logging.warning(f'Publisher: {p} is not in the database')

