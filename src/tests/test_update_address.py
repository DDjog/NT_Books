from src.operations.address_operations import update_address
from src.constans import OPER_IS_IN_DB_FAILED, OPER_UPDATE_SUCCEEDED

a = ['Czerska', '8', '11', '10','00-732', 'Warsaw', 'Poland']
u = update_address ({a})
if u == OPER_UPDATE_SUCCEEDED:
    print(f'Address: {a} is in the database')
elif u == OPER_IS_IN_DB_FAILED:
    print(f'Address: {a} is not in the database')
