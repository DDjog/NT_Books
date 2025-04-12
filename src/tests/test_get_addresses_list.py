import logging
import src.logging_to_file
from src.operations.address_operations import get_addresses_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, addresses_list = get_addresses_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Addresses list was downloaded from the database:')
    for index, address in enumerate(addresses_list, start=1):
        logging.info(f'{index}. {address.street}, {address.number}, {address.flat_number}, {address.zip_code}, {address.city}, '
              f'{address.country}')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('Address list download failed')