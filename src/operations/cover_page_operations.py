import tkinter
import logging
from sqlalchemy.exc import OperationalError
import logging
from src.constans import *
from src.database.models import Book, Cover_page
from src.database.db import session

def add_cover_page(book_id, file_path):
    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        if book:
            with open (file_path, 'rb') as file:
                book.image = file.read()
            session.commit()
            logging.info('Image was added to the book')
            return OPER_ADD_SUCCEEDED, book.id
        else:
            logging.info('No book with ID: {book_id}')
            return OPER_ADD_FAILED_DATA_NOT_IN_DB, None
    except OperationalError as e:
        logging.info(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None
