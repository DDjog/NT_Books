from src.operations.language_operations import update_language
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS

l = ['Polish', 'Spanish']
u = update_language ({l})
if u == OPER_UPDATE_SUCCEEDED:
    print(f'{l} is in the database')
elif u == OPER_UPDATE_FAILED_DATA_NOT_EXISTS:
    print(f'{l} is not in the database')
