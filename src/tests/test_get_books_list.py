from src.operations.books_operations import get_books_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_books_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Books list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Books list download failed')