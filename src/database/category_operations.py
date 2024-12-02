from unicodedata import category

from models import Category
from db import session

def add_category(new_category_name):
    category = session.query(Category).filter_by(category_name=new_category_name).first()

    if not category:
        category = Category(category_name=new_category_name)
        session.add(category)
        session.commit()
        print(f'Category {new_category_name} was added.')
    else:
        print(f'Category {new_category_name} already exists.')

def get_category(category_id):
    category = session.query(Category).filter_by(category_id).first()

    if category:
        print(f'ID: {category_id}, Name: {Category.category_name}')
    else:
        print(f'Category with ID {category_id} was not found')

def get_categories_list():
    categories_list = session.query(Category).all()

    if categories_list:
        print(f'Categories list:')
        for category in categories_list:
            print(f'ID: {category.id}, Name: {category.category_name}')
    else:
        print('Categories list is empty')

def update_category(category_id, updated_category_name):
    category = session.query(Category).filter_by(id=category_id).first()

    if category:
        category.category_name = updated_category_name
        session.commit()
        print(f'Category with ID {category_id} was updated to {updated_category_name}.')
    else:
        print(f'Category with ID {category_id} was not found.')

def delete_category(category_id):
    category = session.query(Category).filter_by(category_id).first()

    if category:
        session.delete(category)
        session.commit()
        print(f'Category of ID {category_id} was deleted.')
    else:
        print(f'Category of ID {category_id} was not found')


