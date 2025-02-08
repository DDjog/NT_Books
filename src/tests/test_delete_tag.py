from src.operations.tag_operations import delete_tag
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

t = 'Heaven'
d = delete_tag({t})
if d == OPER_DELETE_SUCCEEDED:
    print("{t} was deleted from the database")
elif d == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print('{t} doesnt exist in the database')