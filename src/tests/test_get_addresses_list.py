from src.operations.address_operations import get_addresses_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_addresses_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Address list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Address list download failed')