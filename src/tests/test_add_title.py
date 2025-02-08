from src.operations.title_operations import add_title
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

t = 'Outsider'
a = add_title({t})
if a == OPER_ADD_SUCCEEDED:
    print(f'{t} was added to the database')
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{t} already exists in the database')