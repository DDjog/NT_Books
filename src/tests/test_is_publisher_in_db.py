from src.operations.publisher_operations import is_publisher_in_db
from src.constans import OPER_IS_IN_DB_SUCCEEDED, OPER_IS_IN_DB_FAILED

p = ['AXA', '2009']
i = is_publisher_in_db ({p})
if i == OPER_IS_IN_DB_SUCCEEDED:
    print(f'{p} is in the database')
elif i == OPER_IS_IN_DB_FAILED:
    print(f'{p} is not in the database')

