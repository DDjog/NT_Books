from src.operations.tag_operations import get_tags_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

g = get_tags_list()
if g == OPER_GET_LIST_SUCCEEDED:
    print('Tags list was downloaded from the database')
elif g == OPER_GET_LIST_FAILED:
    print('Tags list download failed')