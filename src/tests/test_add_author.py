from src.operations.author_operations import add_author
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

au = ['Vincent', 'Severski']
a = add_author({au})
if a == OPER_ADD_SUCCEEDED:
    print(f"{au} was added to the database")
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'{au} exists already in the database')