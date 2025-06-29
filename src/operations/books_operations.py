
from sqlalchemy.exc import OperationalError
import logging

from src.operations.address_operations import is_address_in_db, add_address
from src.operations.author_operations import is_author_in_db, add_author
from src.operations.category_operations import is_category_in_db, add_category
from src.operations.language_operations import is_language_in_db, add_language
from src.operations.publisher_operations import is_publisher_in_db, add_publisher
from src.operations.title_operations import is_title_in_db, add_title
from src.operations.isbn_operations import is_isbn_in_db, add_isbn
from src.operations.shelf_signature_operations import is_shelf_signature_in_db, add_shelf_signature
from src.operations.tag_operations import is_tag_in_db, add_tag
from src.database.db import session
from src.database.models import Book, Address, Author, Title, Isbn, Language, ShelfSignature, Tag, Publisher, Category, \
    Cover_page
from src.constans import (OPER_DELETE_SUCCEEDED, OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_FOUND,
                          OPER_DELETE_FAILED_DATA_EXISTS, OPER_ADD_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED,
                          OPER_GET_LIST_FAILED, OPER_GET_LIST_SUCCEEDED, OPER_IS_IN_DB_FAILED, OPER_IS_IN_DB_SUCCEEDED,
                          OPER_UPDATE_FAILED_DATA_EXISTS, OPER_ADD_FAILED_NO_DATABASE_CONNECTION,
                          OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, OPER_UPDATE_FAILED_NO_DB_CONNECTION,
                          OPER_DELETE_FAILED_DATA_NOT_FOUND, OPER_DELETE_FAILED_NO_DB_CONNECTION,
                          OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION)



def add_book(new_title, new_author_name, new_author_surname, new_isbn, new_language,
             new_shelf_signature, new_tag, new_publisher,  new_street, new_number, new_flat_number, new_zip_code,
             new_city, new_country, new_publication_year, new_category):

        operation_status = -1
        id = -1
        title = None
        isbn_name = None
        language = None
        shelf_signature = None
        tag = None
        publisher = None
        address = None
        author = None
        category = None
        tag = None

        book = session.query(Book).join(Title).join(Isbn).filter(
            Title.title==new_title,
            Isbn.isbn_name==new_isbn
        ).first()

        if book:
            logging.info('Book is already in the database')
            return OPER_ADD_FAILED_DATA_EXISTS, None

        try:
            new_book = Book()

            title = session.query(Title).filter_by(title=new_title).first()
            if title is None:
                operation_status, id = add_title(new_title)
                new_book.title_id = id
                logging.info('Title was added to the book')
            else:
                logging.info('Title was already added to the book')
                new_book.title_id = title.id


            isbn_name = session.query(Isbn).filter_by(isbn_name=new_isbn).first()
            if isbn_name is None:
                operation_status, id = add_isbn(new_isbn)
                new_book.isbn_id = id
                logging.info('Isbn was added to the book')
            else:
                logging.info('Isbn was already added to the book')
                new_book.isbn_id = isbn_name.id

            language = session.query(Language).filter_by(language=new_language).first()
            operation_status, id = is_language_in_db(new_language)
            if not operation_status == OPER_IS_IN_DB_SUCCEEDED:
                operation_status, language_id = add_language(new_language)
                new_book.language_id = language_id
                logging.info('Language was added to the book')
            else:
                new_book.language_id = language.id
                logging.info('Language exists in the database and was added to the book ')


            shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=new_shelf_signature).first()
            if shelf_signature is None:
                operation_status, shelf_signature_id = add_shelf_signature(new_shelf_signature)
                new_book.shelf_signature_id = shelf_signature_id
                logging.info('Shelf signature was added to the book')
            else:
                new_book.shelf_signature_id = shelf_signature.id
                logging.info('Shelf signature exists in the database and was added to the book')


            address = session.query(Address).filter_by(
                street=new_street,
                number=new_number,
                flat_number=new_flat_number,
                zip_code=new_zip_code,
                city=new_city,
                country=new_country
            ).first()
            if address is None:
                operation_status, new_address_id = add_address(new_street, new_number, new_flat_number,new_zip_code,
                                                               new_city, new_country)
                logging.info('New address was added to the database')
            else:
                new_address_id = address.id
                logging.info('Address exists in the database')


            publisher = session.query(Publisher).filter_by(
                publisher=new_publisher,
                publication_year = new_publication_year,
                address_id=new_address_id
            ).first()
            if publisher is None:
                operation_status, id = add_publisher(new_publisher, new_publication_year, new_address_id)
                new_book.publisher_id = id
                logging.info('New publisher was added to the book')
            else:
                new_book.publisher_id = publisher.id
                logging.info('Publisher exists in the database and was added to the book')

            session.add(new_book)
            session.commit()


            # relation to author
            author = session.query(Author).filter_by(
                author_name=new_author_name,
                author_surname=new_author_surname
            ).first()
            if author is None:
                operation_status, author_id = add_author(new_author_name, new_author_surname)
                logging.info('New author was added to the book')
                new_author = session.query(Author).filter_by(id=author_id).first()
            else:
                new_author=author
                logging.info('Author exists in the database and was added to the book')

            # relation to category
            category = session.query(Category).filter_by(category_name=new_category).first()
            if category is None:
                operation_status, category_id = add_category(category_name=new_category)
                logging.info('New category was added to the book')
                new_category = session.query(Category).filter_by(id=category_id).first()
            else:
                new_category=category


            # relation to tag
            tag = session.query(Tag).filter_by(tag=new_tag).first()
            if tag is None:
                operation_status, tag_id = add_tag(tag_name=new_tag)
                logging.info('New tag was added to the book')
                new_tag = session.query(Tag).filter_by(id=tag_id).first()
            else:
                new_tag=tag


            new_book.authors.append(new_author)
            logging.info('Author exists in the database and was added to the book')
            new_book.categories.append(new_category)
            logging.info('Category exists in the database and was added to the book')
            new_book.tags.append(new_tag)
            logging.info('Tag exists in the database and was added to the book')
            session.commit()

            return OPER_ADD_SUCCEEDED, new_book.id

        except OperationalError as e:
            session.rollback()
            logging.info('No database connection: {e}')
            return OPER_ADD_FAILED_NO_DATABASE_CONNECTION


def is_book_in_db(title, isbn):
    try:
        book = session.query(Book).join(Title).join(Isbn).filter(
            Title.title==title,
            Isbn.isbn_name==isbn
            ).first()
        if book:
            logging.info('Book is in the database')
            return OPER_IS_IN_DB_SUCCEEDED, book.id
        else:
            logging.info('Book is not in the database')
            return OPER_IS_IN_DB_FAILED, None
    except OperationalError as e:
        logging.error(f'No database connection: {e}')
        return OPER_IS_IN_DB_FAILED_NO_DB_CONNECTION, None


def get_books_list():
    try:
        books_list = session.query(Book).join(Title).join(Isbn).all()

        if books_list:
            logging.info('Book list got')
            return OPER_GET_LIST_SUCCEEDED, books_list
        else:
            logging.info('Book list failed')
            return OPER_GET_LIST_FAILED, None
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_GET_LIST_FAILED_NO_DATABASE_CONNECTION, None


def update_book(old_title, new_title, old_author_name, new_author_name, old_author_surname, new_author_surname, old_isbn,
                new_isbn, old_language, new_language, old_shelf_signature, new_shelf_signature, old_tag, new_tag,
                old_publisher, new_publisher, old_street, new_street, old_number, new_number, old_flat_number, new_flat_number,
                old_zip_code, new_zip_code, old_city, new_city, old_country, new_country, old_publication_year,
                new_publication_year, old_category, new_category):
    existing_isbn = session.query(Isbn).filter(Isbn.isbn_name == new_isbn).first()


    if existing_isbn and existing_isbn.id != Book.isbn_id:
        return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None

    try:
        session.commit()
    except:
        session.rollback()
        logging.error(f'New isbn exists already: {new_isbn}')
        return OPER_UPDATE_FAILED_DATA_EXISTS, None

    try:
        book = session.query(Book).join(Title).join(Isbn).filter(
            Title.title==old_title,
            Isbn.isbn_name==old_isbn
        ).first()

        if not book:
            return OPER_UPDATE_FAILED_DATA_NOT_FOUND, None

        title = session.query(Title).filter(Title.title == old_title).first()
        if book.title:
            book.title.title = new_title

        isbn = session.query(Isbn).filter(Isbn.isbn_name == old_isbn).first()
        if isbn:
            book.isbn.isbn_name = new_isbn

        author = session.query(Author).filter(
            Author.author_name==old_author_name,
            Author.author_surname==old_author_surname
        ).first()
        if author:
            author.author_name = new_author_name
            author.author_surname = new_author_surname

        language = session.query(Language).filter(Language.language==old_language).first()
        if language:
            language.language = new_language

        shelf_signature = session.query(ShelfSignature).filter(ShelfSignature.shelf_signature==old_shelf_signature).first()
        if shelf_signature:
            shelf_signature.shelf_signature = new_shelf_signature

        tag = session.query(Tag).filter(Tag.tag==old_tag).first()
        if tag:
            tag.tag = new_tag

        publisher = session.query(Publisher).filter(
            Publisher.publisher==old_publisher,
            Publisher.publication_year==old_publication_year).first()
        if publisher:
            publisher.publisher = new_publisher
            publisher.publication_year = new_publication_year

        address = session.query(Address).filter(
            Address.street==old_street,
            Address.number==old_number,
            Address.flat_number==old_flat_number,
            Address.zip_code==old_zip_code,
            Address.city==old_city,
            Address.country==old_country
        )
        if address:
            address.street = new_street
            address.number = new_number
            address.flat_number = new_flat_number
            address.zip_code = new_zip_code
            address.city = new_city
            address.country = new_country

        category = session.query(Category).filter(Category.category_name==old_category).first()
        if category:
            category.categories=new_category

        session.commit()
        logging.info('Book was updated')
        return OPER_UPDATE_SUCCEEDED, book.id

    except OperationalError as e:
        session.rollback()
        logging.info(f'No database connection: {e}')
        return OPER_UPDATE_FAILED_NO_DB_CONNECTION, None


def delete_book(title, isbn):
    try:
        book = session.query(Book).join(Title).join(Isbn).filter(
            Title.title == title,
            Isbn.isbn_name == isbn
        ).first()

        if book:
            session.delete(book)
            session.commit()
            logging.info('Book was deleted')
            return OPER_DELETE_SUCCEEDED
        else:
            logging.info('Data not found')
            return OPER_DELETE_FAILED_DATA_NOT_FOUND
    except OperationalError as e:
        logging.error(f'Database error connection: {e}')
        return OPER_DELETE_FAILED_NO_DB_CONNECTION






