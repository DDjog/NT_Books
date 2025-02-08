from src.operations.tag_operations import add_tag
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

t = 'New Year'
a = add_tag({t})
if a == OPER_ADD_SUCCEEDED:
    print(f'{t} was added to the database')
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{t} already exists in the database')