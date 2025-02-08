from src.operations.language_operations import get_languages_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_languages_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Languages list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Languages list download failed')