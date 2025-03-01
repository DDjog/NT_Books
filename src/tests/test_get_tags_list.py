from src.operations.tag_operations import get_tags_list
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status, tags_list = get_tags_list()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    print('Tags list was downloaded from the database:')
    for index, tag in enumerate(tags_list, start=1):
        print(f'{index}. {tag.tag}')
elif operation_status == OPER_GET_LIST_FAILED:
    print('Tags list download failed')