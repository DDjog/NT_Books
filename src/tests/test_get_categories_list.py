from src.operations.category_operations import get_categories_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_categories_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Categories list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Categories list download failed')