from src.operations.category_operations import delete_category
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

c = 'Poetry'
d = delete_category({c})
if d == OPER_DELETE_SUCCEEDED:
    print("{c} was deleted from the database")
elif d == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print('{c} doesnt exist in the database')