from src.operations.books_operations import delete_book
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS

b = ['FHow to solve your own murder', 'F978-1-52943-007-3']
title, isbn = b
operation_system = delete_book(title, isbn)
if operation_system == OPER_DELETE_SUCCEEDED:
    print(f"{b} was deleted from the database")
elif operation_system == OPER_DELETE_FAILED_DATA_NOT_EXISTS:
    print(f'{b} exists not in the database')