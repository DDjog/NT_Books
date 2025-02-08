from src.operations.category_operations import is_category_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

c = ['Fairy Tale']
i = is_category_in_db({c})
if i == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{c} is in the database')
elif i == OPER_IS_IN_DB_FAILED:
    print(f'{c} is not in the database')