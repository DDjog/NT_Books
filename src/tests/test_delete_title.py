from src.operations.title_operations import delete_title
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

t = 'Dark moon'
d = delete_title({t})
if d == OPER_DELETE_SUCCEEDED:
    print("{t} was deleted from the database")
elif d == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print('{t} doesnt exist in the database')