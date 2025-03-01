from src.operations.tag_operations import delete_tag
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

t = 'New Year'
operation_status = delete_tag(t)
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f"{t} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'{t} doesnt exist in the database')