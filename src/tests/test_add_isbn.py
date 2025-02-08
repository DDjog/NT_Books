from src.operations.isbn_operations import add_isbn
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

i = '765-88-54-00000-1'
a = add_isbn({i})
if a == OPER_ADD_SUCCEEDED:
    print(f"{i} was added to the database")
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{i} exists already in the database')