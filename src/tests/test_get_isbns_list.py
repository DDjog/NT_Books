from src.operations.isbn_operations import get_isbn_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED


operation_status, isbns_list = get_isbn_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    print('Isbn list was downloaded from the database:')
    for index, isbn in enumerate(isbns_list, start=1):
        print(f'{index}. {isbn.isbn_name} ')
elif operation_status == OPER_GET_LIST_FAILED:
    print('Isbn list download failed')