from src.operations.language_operations import is_language_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

l = 'Spanish'
i = is_language_in_db ({l})
if i == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{l} is in the database')
elif i == OPER_IS_IN_DB_FAILED:
    print(f'{l} is not in the database')