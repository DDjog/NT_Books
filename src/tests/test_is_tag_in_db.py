from src.operations.tag_operations import is_tag_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

t = 'New Year'
operation_status, tag_id = is_tag_in_db (t)
if operation_status== OPER_IS_IN_DB_SUCCEEDED:
    print(f'{t} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    print(f'{t} is not in the database')

