from src.operations.author_operations import add_author
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

au = 'Vincent', 'Severski'
name, surname = au
operation_status, author_id = add_author(name, surname)
if operation_status == OPER_ADD_SUCCEEDED:
    print(f'Author {name} {surname} was added to the database')
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
    print(f'Author {name} {surname} is already in the database')