from src.operations.language_operations import add_language
from src.constans import  *

l='Turkish'
a = add_language(l)

if a == OPER_ADD_SUCCEEDED:
    print(f'{l} was added to the database')
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{l} already exists in the database')
