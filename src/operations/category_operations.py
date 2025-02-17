from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, \
    OPER_UPDATE_SUCCEEDED, OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS
from src.database.models import Category
from src.database.db import session

def add_category(category_name):
    category = session.query(Category).filter_by(category_name=category_name).first()

    if not category:
        category = Category(category_name=category_name)
        session.add(category)
        session.commit()
        return OPER_ADD_SUCCEEDED, category.id
    return OPER_ADD_FAILED_DATA_EXISTS, category.id

def is_category_in_db(category_name):
    category = session.query(Category).filter_by(category_name=category_name).first()

    if category:
        _id = category.id
        print(f'ID: {_id}, Category name: {category_name}')
        return True
    return False

def get_categories_list():
    categories_list = session.query(Category).all()

    if categories_list:
        print(f'Categories list:')
        for category in categories_list:
            _id = category.id
            print(f'ID: {_id}, Name: {category.category_name}')
        return categories_list
    return OPER_GET_LIST_FAILED

def update_category(old_category_name, updated_category_name):
    category = session.query(Category).filter_by(category_name=old_category_name).first()

    if category:
        _id = category.id
        category.category_name = updated_category_name
        session.commit()
        print(f'ID: {_id}, Category: {old_category_name} was updated to {updated_category_name}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_ADD_FAILED_DATA_EXISTS

def delete_category(category_name):
    category = session.query(Category).filter_by(category_name=category_name).first()

    if category:
        _id=category.id
        session.delete(category)
        session.commit()
        print(f'ID: {_id}, Category: {category_name} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS

