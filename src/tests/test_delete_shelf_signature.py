from src.operations.shelf_signature_operations import delete_shelf_signature
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

s = '54678'
operation_status = delete_shelf_signature(s)
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f"Shelf signature: {s} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'Shelf signature: {s} doesnt exist in the database')