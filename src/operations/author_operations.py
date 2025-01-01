
from src.database.models import Author
from src.database.db import session

def add_author(new_author_name, new_author_surname):
    author_name = session.query(Author).filter_by(category_name=new_author_name).first()
    author_surname = session.query(Author).filter_by(category_name=new_author_surname).first()

    if not (author_name and author_surname):
        author_name = Author(author_name=new_author_name)
        author_surname = Author(author_name=new_author_surname)
        session.add(author_name)
        session.add(author_surname)
        session.commit()
        print(f'Author {new_author_name} {new_author_surname} was added.')
    else:
        print(f'Author {new_author_name} {new_author_surname} already exists.')

def get_author(aut_name, aut_surname):
    author_name = session.query(Author).filter_by(category_name=aut_name).first()
    author_surname = session.query(Author).filter_by(category_name=aut_surname).first()

    if author_name and author_surname:
        print(f'Author name: {aut_name}, Author surname: {aut_surname}, ID: {Author.id}')
    else:
        print(f'Author {aut_name} {aut_surname} was not found')

def get_authors_list():
    authors_name_list = session.query(Author.author_name).all()
    authors_surname_list = session.query(Author.author_surname).all()

    if authors_name_list and authors_surname_list:
        print(f'Authors list:')
        for author_name in authors_name_list:
            for author_surname in authors_surname_list:
                print(f'ID: {Author.id}, Name and surname: {Author.author_name} {Author.author_surname}')
            return authors_name_list, authors_surname_list
    else:
        print('Authors list is empty')
        return None

def update_author(aut_name, aut_surname, updated_aut_name, updated_aut_surname):
    author_name = session.query(Author).filter_by(category_name=aut_name).first()

    if category:
        category.category_name = updated_category_name
        session.commit()
        print(f'Category: {id} {cat_name} was updated to {updated_category_name}.')
    else:
        print(f'Category {cat_name} was not found.')

def delete_author(cat_name):
    category = session.query(Category).filter_by(category_name=cat_name).first()

    if category:
        _id=category.id
        session.delete(category)
        session.commit()
        print(f'Category: {_id} {cat_name} was deleted.')
    else:
        print(f'Category {cat_name} was not found.')


