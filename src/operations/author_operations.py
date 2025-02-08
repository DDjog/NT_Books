from src.constans import (OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_ADD_SUCCEEDED,
                          OPER_ADD_FAILED_DATA_EXISTS, OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS, \
    OPER_GET_LIST_FAILED)
from src.database.models import Author
from src.database.db import session

def add_author(indicated_author_name, indicated_author_surname):
    author = session.query(Author).filter_by(author_name=indicated_author_name, author_surname=indicated_author_surname).first()

    if not author:
        author = Author(author_name=indicated_author_name,
                            author_surname=indicated_author_surname)
        session.add(author)
        session.commit()
        return OPER_ADD_SUCCEEDED, author.id
    return OPER_ADD_FAILED_DATA_EXISTS, author.id

def is_author_in_db(indicated_author_name, indicated_author_surname):
    author = session.query(Author).filter_by(author_name=indicated_author_name, author_surname=indicated_author_surname).first()

    if author:
        _id = author.id
        print(f'ID: {_id}, Author name: {indicated_author_name} Author surname: {indicated_author_surname}')
        return True
    return False

def get_authors_list():
    authors_list = session.query(Author).all()

    if authors_list:
        print(f'Authors list:')
        for author in authors_list:
            _id = author.id
            print(f'ID: {_id}, Name and surname: {author.author_name} {author.author_surname}')
        return authors_list
    return OPER_GET_LIST_FAILED

def update_author(old_author_name, old_author_surname, updated_author_name, updated_author_surname):
    author = session.query(Author).filter_by(author_name=old_author_name, author_surname=old_author_surname).first()

    if author:
        _id = author.id
        author.author_name = updated_author_name,
        author.author_surname = updated_author_surname
        session.commit()
        print(f'(ID: {_id}), Author: {old_author_name} {old_author_surname}  was updated to {updated_author_name} {updated_author_surname}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_author(indicated_author_name, indicated_author_surname):
    author = session.query(Author).filter_by(author_name=indicated_author_name, author_surname=indicated_author_surname).first()

    if author:
        _id=author.id
        session.delete(author)
        session.commit()
        print(f'ID: {_id}, Author: {indicated_author_name} {indicated_author_surname}  was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS


