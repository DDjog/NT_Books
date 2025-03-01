from src.operations.category_operations import add_category
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

c = 'Poetry'
operation_status, category_id = add_category(c)
if operation_status == OPER_ADD_SUCCEEDED:
    print(f'{c} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{c} exists already in the database')