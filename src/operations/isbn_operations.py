from src.database.models import Isbn
from src.database.db import session

def add_isbn(isbn_number):
    if len(isbn_number) == 17:
        isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()

        if not isbn:
            isbn = Isbn(isbn_name=isbn_number)
            session.add(isbn)
            session.commit()
            print(f'ISBN: {isbn_number} was added.')
        else:
            print(f'ISBN: {isbn_number} already exists in database.')
    else:
        print('ISBN number incorrect')

def is_isbn_in_db(isbn_number):
    isbn = session.query(Isbn).filter_by(isbn_name=isbn_number).first()

    if isbn:
        print(f'ISBN: {isbn_number} is already in database')
        return True
    print('ISBN number not in db')
    return False
