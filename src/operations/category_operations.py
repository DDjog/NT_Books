
from src.database.models import Category
from src.database.db import session

def add_category(category_name):
    category = session.query(Category).filter_by(category_name=category_name).first()

    if not category:
        category = Category(category_name=category_name)
        session.add(category)
        session.commit()
        print(f'Category {category_name} was added.')
    else:
        print(f'Category {category_name} already exists.')

def find_category(category_name):
    category = session.query(Category).filter_by(category_name=category_name).first()

    if category:
        print(f'Category name: {category_name}, ID: {category.id}')
    else:
        print(f'Category name {category_name} was not found')

def get_categories_list():
    categories_list = session.query(Category).all()

    if categories_list:
        print(f'Categories list:')
        for category in categories_list:
            print(f'ID: {category.id}, Name: {category.category_name}')
        return categories_list
    else:
        print('Categories list is empty')
        return None

def update_category(old_category_name, updated_category_name):
    category = session.query(Category).filter_by(category_name=old_category_name).first()

    if category:
        category.category_name = updated_category_name
        session.commit()
        print(f'Category: {id} {old_category_name} was updated to {updated_category_name}.')
    else:
        print(f'Category {old_category_name} was not found.')

def delete_category(category_name):
    category = session.query(Category).filter_by(category_name=category_name).first()

    if category:
        _id=category.id
        session.delete(category)
        session.commit()
        print(f'Category: {_id} {category_name} was deleted.')
    else:
        print(f'Category {category_name} was not found.')


