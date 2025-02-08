from src.operations.author_operations import get_authors_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_authors_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Authors list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Authors list download failed')