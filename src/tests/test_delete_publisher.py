import logging
import src.logging_to_file
from src.operations.publisher_operations import delete_publisher
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_FOUND

p = ['AXA', 2009]
publisher, publication_year = p
operation_status = delete_publisher(publisher, publication_year)
if operation_status == OPER_DELETE_SUCCEEDED:
    logging.info(f"Publisher: {publisher} with publication year {publication_year} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_FOUND:
    logging.warning(f'Publisher: {publisher} with publication year {publication_year} doesnt exist in the database')