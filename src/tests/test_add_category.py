from src.operations.category_operations import add_category
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

c = 'Poetry'
a = add_category({c})
if a == OPER_ADD_SUCCEEDED:
    print(f'{c} was added to the database')
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{c} exists already in the database')