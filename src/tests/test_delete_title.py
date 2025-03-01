from src.operations.title_operations import delete_title
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS
from src.tests.test_delete_book import operation_system

t = 'Outsider'
operation_status = delete_title(t)
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f"{t} was deleted from the database")
elif operation_system == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'{t} doesnt exist in the database')