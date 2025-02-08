from src.operations.address_operations import add_address
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

ad = ['Czerska', '8', '10', '00-732', 'Warsaw', 'Poland']
a = add_address({ad})
if a == OPER_ADD_SUCCEEDED:
    print("New address was added to the database")
elif a == OPER_ADD_FAILED_DATA_EXISTS:
    print('New address exists already in the database')