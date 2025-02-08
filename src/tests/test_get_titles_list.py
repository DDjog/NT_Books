from src.operations.title_operations import get_titles_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_titles_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Titles list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Titles list download failed')