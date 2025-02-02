from src.database.models import Isbn
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, \
    OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_NOT_EXISTS, OPER_ADD_SUCCEEDED


def add_isbn(isbn_number):
    # if len(isbn_number) == 17:
    isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()

    if not isbn:
        isbn = Isbn(isbn_name=isbn_number)
        session.add(isbn)
        session.commit()
        print(f'ISBN: {isbn_number} was added.')
        return OPER_ADD_SUCCEEDED
    return OPER_ADD_FAILED_DATA_EXISTS


def is_isbn_in_db(isbn_number):
    isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()

    if isbn:
        print(f'ISBN: {isbn_number} is already in database')
        return True
    return False

def get_isbn_list():
    isbns_list = session.query(Isbn).all()

    if isbns_list:
        print(f'ISBNs list:')
        for isbn in isbns_list:
            _id = isbn.id
            print(f'ID: {_id}, ISBN: {isbn.isbn}')
        return isbns_list
    return OPER_GET_LIST_FAILED

def update_isbn(old_isbn_number, new_isbn_number):
    isbn = session.query(Isbn).filter_by(isbn=old_isbn_number).first()

    if isbn:
        _id = isbn.id
        isbn.isbn = new_isbn_number
        session.commit()
        print(f'ID: {_id}, ISBN: {old_isbn_number} was updated to {new_isbn_number}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_isbn(isbn_name):
    isbn = session.query(Isbn).filter_by(isbn=isbn_name).first()

    if isbn:
        _id=isbn.id
        session.delete(isbn)
        session.commit()
        print(f'ID: {_id}, ISBN: {isbn} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS