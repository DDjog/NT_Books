from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS
from src.operations.address_operations import delete_address


ad = ['Czerska', '8', '10', '00-732', 'Warsaw', 'Poland']
d = delete_address({ad})
if d == OPER_DELETE_SUCCEEDED:
    print("New address was deleted from the database")
elif d == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print('New address doesnt exist in the database')