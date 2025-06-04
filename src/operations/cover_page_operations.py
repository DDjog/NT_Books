import io
import tkinter
import logging
from sqlalchemy.exc import OperationalError
import logging
from src.constans import *
from src.database.models import Book, Cover_page
from src.database.db import session
from PIL import Image, ImageTk
from tkinter import Toplevel, Label



def add_cover_page(file_path):
    try:
        with open(file_path, 'rb') as file:
            new_cover_page = file.read()
        cover_page = session.query(Cover_page).filter_by(cover_page=new_cover_page).first()
        if not cover_page:
            new_cover_page = Cover_page(cover_page=new_cover_page)
            session.add(new_cover_page)
            session.commit()
            logging.info('Cover page was added to the book')
            return OPER_ADD_SUCCEEDED, new_cover_page.id
        else:
            logging.info('Cover page exists in database')
            return OPER_ADD_FAILED_DATA_EXISTS, cover_page.id
    except OperationalError as e:
        logging.info(f'No database connection: {e}')
        session.rollback()
        return OPER_ADD_FAILED_NO_DATABASE_CONNECTION, None

def get_cover_page(cover_page_id, output_path):
    try:
        cover_page = session.query(Cover_page).filter_by(id = cover_page_id).first()
        if cover_page:
            with open(output_path, 'wb') as file:
                file.write(cover_page.cover_page)
            logging.info(f'Cover page obtained and saved to {output_path}')
            return OPER_GET_LIST_SUCCEEDED, output_path
        else:
            logging.info('Cover page failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def get_cover_page_display_in_GUI():
    try:
        cover_pages = session.query(Cover_page).all()
        if cover_pages:
            for cp in cover_pages:
                window = Toplevel()
                window.title(f'Cover page ID: {cp.id}')
                image = Image.open(io.BytesIO(cp.cover_page))
                image = image.resize((200, 250))
                photo = ImageTk.PhotoImage(image)

                label = Label(window, image=photo)
                label.image = photo
                label.pack(padx=10, pady=10)
            logging.info(f'All cover pages were displayed')
            return OPER_GET_LIST_SUCCEEDED
        else:
            logging.info('Cover page failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def get_cover_page_list():
    try:
        cover_page_list = session.query(Cover_page).all()
        if cover_page_list:
            logging.info(' Cover page list obtained')
            return OPER_GET_LIST_SUCCEEDED, cover_page_list
        else:
            logging.info('Cover page list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None

def update_book_with_cover_page(new_cover_page_id, book_id):
    try:
        book = session.query(Book).filter_by(id = book_id).first()
        cover_page = session.query(Cover_page).filter_by(id=new_cover_page_id).first()
        if book:
            cover_page.book = book
            session.commit()
            logging.info(f'Cover page with ID: {new_cover_page_id} was added to book with ID: {book_id}')
            return OPER_UPDATE_SUCCEEDED
        else:
            logging.info(f'Book with ID: {book_id} not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION

def update_cover_page(old_file_path, new_file_path):
    try:
        with open(old_file_path, 'rb') as file:
            old_file = file.read()
        with open(new_file_path, 'rb') as file:
            new_file = file.read()
        cover_page = session.query(Cover_page).filter_by(cover_page=old_file).first()
        if cover_page:
            cover_page.cover_page = new_file
            session.commit()
            logging.info('Cover page was updated')
            return OPER_UPDATE_SUCCEEDED, cover_page.id
        else:
            logging.info('Data not found')
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None
    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None

def delete_cover_page(file_path):
    try:
        with open(file_path, 'rb') as file:
            cover_page_d = file.read()
            cover_page_to_be_deleted = session.query(Cover_page).filter_by(cover_page=cover_page_d).first()
        if cover_page_to_be_deleted:
            session.delete(cover_page_to_be_deleted)
            session.commit()
            logging.info(f'Cover page with ID: {cover_page_to_be_deleted.id} deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Cover page not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION

