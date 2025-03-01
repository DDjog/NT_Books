from src.operations.category_operations import delete_category
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

c = 'Poetry'
operation_status = delete_category(c)
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f"{c} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'{c} doesnt exist in the database')