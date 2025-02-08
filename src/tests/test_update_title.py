from src.operations.title_operations import update_title
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS

t = ['Outsider', 'Outsiders']
u = update_title ({t})
if u == OPER_UPDATE_SUCCEEDED:
    print(f'{t} is in the database')
elif u == OPER_UPDATE_FAILED_DATA_NOT_EXISTS:
    print(f'{t} is not in the database')
