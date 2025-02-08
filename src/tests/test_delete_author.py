from src.operations.author_operations import delete_author
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

au = ['Alfred', 'Forsyth']
d = delete_author({au})
if d == OPER_DELETE_SUCCEEDED:
    print("{au} was deleted from the database")
elif d == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print('{au} doesnt exist in the database')