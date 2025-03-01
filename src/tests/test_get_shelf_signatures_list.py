from src.operations.shelf_signature_operations import get_shelf_signatures_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED


operation_status, shelf_signatures_list = get_shelf_signatures_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    print('Shelf signatures list was downloaded from the database:')
    for index, shelf_signature in enumerate(shelf_signatures_list, start=1):
        print(f'{index}. {shelf_signature.shelf_signature} ')
elif operation_status == OPER_GET_LIST_FAILED:
    print('IShelf signatures list download failed')