from src.operations.category_operations import update_category
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND
from src.tests.test_update_book import old_category

c = ['Poetry','Comedy']
old_category_name, updated_category_name = c
operation_status, category_id = update_category(old_category_name, updated_category_name)
if operation_status == OPER_UPDATE_SUCCEEDED:
    print(f'Updated category {updated_category_name} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_NOT_FOUND:
    print(f'Category {updated_category_name} is not in the database')
