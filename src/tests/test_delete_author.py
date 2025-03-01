from src.operations.author_operations import delete_author
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

a = ['Vincentt', 'Severskiii']
author_name, author_surname = a
operation_status = delete_author(author_name, author_surname)
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f'{a} was deleted from the database')
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'{a} exists not in the database')