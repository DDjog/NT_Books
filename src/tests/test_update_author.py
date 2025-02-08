from src.operations.author_operations import update_author
from src.constans import OPER_IS_IN_DB_FAILED, OPER_UPDATE_SUCCEEDED

a = ['Frederick', 'Forsyth', 'Alfred', 'Forsyth']
u = update_author ({a})
if u == OPER_UPDATE_SUCCEEDED:
    print(f'Address: {a} is in the database')
elif u == OPER_IS_IN_DB_FAILED:
    print(f'Address: {a} is not in the database')
