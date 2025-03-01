from src.operations.publisher_operations import delete_publisher
from src.constans import OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_EXISTS

p = ['AXA', 2009]
publisher, publication_year = p
operation_status = delete_publisher(publisher, publication_year)
print(f'operation_status: {operation_status}, publication_year: {publication_year}')
if operation_status == OPER_DELETE_SUCCEEDED:
    print(f"Publisher: {publisher} with publication year {publication_year} was deleted from the database")
elif operation_status == OPER_DELETE_FAILED_DATA_EXISTS:
    print(f'Publisher: {publisher} with publication year {publication_year} doesnt exist in the database')