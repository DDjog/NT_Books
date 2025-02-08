from src.operations.address_operations import is_address_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

a = ['Czerska', '8', '10', '00-732', 'Warsaw', 'Poland']
i = is_address_in_db({a})
if i == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{a} is in the database')
elif i == OPER_IS_IN_DB_FAILED:
    print(f'{a} is not in the database')