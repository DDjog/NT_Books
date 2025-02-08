from src.operations.category_operations import update_category
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS

c = ['Comedy', 'Poetry']
u = update_category ({c})
if u == OPER_UPDATE_SUCCEEDED:
    print(f'{c} is in the database')
elif u == OPER_UPDATE_FAILED_DATA_NOT_EXISTS:
    print(f'{c} is not in the database')
