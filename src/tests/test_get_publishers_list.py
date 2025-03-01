from src.operations.publisher_operations import get_publishers_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED


operation_status, publisher_list = get_publishers_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    print('Publishers list was downloaded from the database:')
    for index, publisher in enumerate(publisher_list, start=1):
        print(f'{index}. {publisher.publisher}, {publisher.publication_year}')
elif operation_status == OPER_GET_LIST_FAILED:
    print('Address list download failed')