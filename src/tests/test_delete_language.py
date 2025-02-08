from src.operations.language_operations import delete_language
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

l = 'Polish'
d = delete_language({l})
if d == OPER_DELETE_SUCCEEDED:
    print("{l} was deleted from the database")
elif d == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print('{l} doesnt exist in the database')
