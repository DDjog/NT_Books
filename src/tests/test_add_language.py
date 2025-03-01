from src.operations.language_operations import add_language
from src.constans import  *

l='Turkish'
operation_status, language_id = add_language(l)

if operation_status == OPER_ADD_SUCCEEDED:
    print(f'{l} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{l} already exists in the database')
