from src.operations.language_operations import delete_language
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

l = 'Turkish'
operation_status = delete_language(l)
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f"{l} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'{l} doesnt exist in the database')
