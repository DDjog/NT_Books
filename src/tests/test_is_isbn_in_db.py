from src.operations.isbn_operations import is_isbn_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

isn = '978-3-16-148410-0'
i = is_isbn_in_db ({isn})
if i == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{isn} is in the database')
elif i == OPER_IS_IN_DB_FAILED:
    print(f'{isn} is not in the database')