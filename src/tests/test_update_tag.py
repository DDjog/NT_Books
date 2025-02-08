from src.operations.tag_operations import update_tag
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS

t = ['Heaven', 'Forest']
u = update_tag ({t})
if u == OPER_UPDATE_SUCCEEDED:
    print(f'{t} is in the database')
elif u == OPER_UPDATE_FAILED_DATA_NOT_EXISTS:
    print(f'{t} is not in the database')
