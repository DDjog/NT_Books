from src.operations.author_operations import is_author_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

a = ['John', 'Smith']
i = is_author_in_db({a})
if i == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{a} is in the database')
elif i == OPER_IS_IN_DB_FAILED:
    print(f'{a} is not in the database')