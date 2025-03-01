from src.operations.category_operations import get_categories_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, categories_list = get_categories_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    print('Categories list was downloaded from the database:')
    for index, category in enumerate(categories_list, start=1):
        print(f'{index}. {category.category_name} ')
elif operation_status == OPER_GET_LIST_FAILED:
    print('Categories list download failed')