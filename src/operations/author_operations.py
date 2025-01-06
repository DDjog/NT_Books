from unicodedata import category

from src.database.models import Author
from src.database.db import session

def add_author(indicated_author_name, indicated_author_surname):
    author = session.query(Author).filter_by(author_name=indicated_author_name, author_surname=indicated_author_surname).first()

    if not author:
        new_author = Author(author_name=indicated_author_name,
                            author_surname=indicated_author_surname)
        session.add(new_author)
        session.commit()
        print(f'Author {indicated_author_name} {indicated_author_name} was added.')
    else:
        print(f'Author {indicated_author_name} {indicated_author_surname} already exists.')

def find_author_id(indicated_author_name, indicated_author_surname):
    author = session.query(Author).filter_by(author_name=indicated_author_name, author_surname=indicated_author_surname).first()

    if author:
        print(f'Author name: {indicated_author_name} Author surname: {indicated_author_surname}, ID: {Author.id}')
    else:
        print(f'Author {indicated_author_name} {indicated_author_surname} was not found')

def get_authors_list():
    authors_list = session.query(Author).all()

    if authors_list:
        print(f'Authors list:')
        for author in authors_list:
            print(f'ID: {author.id}, Name and surname: {author.author_name} {author.author_surname}')
        return authors_list
    else:
        print('Authors list is empty')
        return None

def update_author(old_author_name, old_author_surname, updated_author_name, updated_author_surname):
    author = session.query(Author).filter_by(author_name=old_author_name, author_surname=old_author_surname).first()

    if author:
        author.author_name = updated_author_name,
        author.author_surname = updated_author_surname
        session.commit()
        print(f'Category: {id} {old_author_name} {old_author_surname} was updated to {updated_author_name} {updated_author_surname}.')
    else:
        print(f'Category {old_author_name} {old_author_surname} was not found.')

def delete_author(indicated_author_name, indicated_author_surname):
    author = session.query(Author).filter_by(author_name=indicated_author_name, author_surname=indicated_author_surname).first()

    if author:
        _id=author.id
        session.delete(author)
        session.commit()
        print(f'Category: {_id} {indicated_author_name} {indicated_author_surname} was deleted.')
    else:
        print(f'Category {indicated_author_name} {indicated_author_surname} was not found.')


