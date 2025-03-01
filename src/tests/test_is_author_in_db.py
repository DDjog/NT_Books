from src.operations.author_operations import is_author_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED
from src.tests.test_delete_isbn import operation_status

a = ['John', 'Smith']
author_name, author_surname = a
operation_system, author_id = is_author_in_db(author_name, author_surname)
if operation_status == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{a} is in the database')
elif operation_status == OPER_IS_IN_DB_FAILED:
    print(f'{a} is not in the database')