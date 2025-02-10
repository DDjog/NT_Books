from unicodedata import category

from matplotlib.pyplot import title

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
    book_m2m_author, book_m2m_tag, book_m2m_category
from src.constans import (OPER_DELETE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS , OPER_DELETE_SUCCEEDED, OPER_UPDATE_SUCCEEDED, \
    OPER_ADD_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS, OPER_UPDATE_FAILED_DATA_NOT_EXISTS,
                          OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_FAILED)


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


    new_book = Book()

    title = session.query(Title).filter_by(title=new_title).first()
    if title is None:
        operation_status, id = add_title(new_title)
        new_book.title_id = id
    else:
        new_book.title_id = title.id


    isbn_name = session.query(Isbn).filter_by(isbn_name=new_isbn).first()
    if isbn_name is None:
        operation_status, id = add_isbn(new_isbn)
        new_book.isbn_id = id
    else:
        new_book.isbn_id = isbn_name.id


    language = session.query(Language).filter_by(language=new_language).first()
    if language is None:
        operation_status, id = add_language(new_language)
        new_book.language_id = id
    else:
        new_book.language_id = language.id


    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=new_shelf_signature).first()
    if shelf_signature is None:
        operation_status, id = add_shelf_signature(new_shelf_signature)
        new_book.shelf_signature_id = id
    else:
        new_book.shelf_signature_id = shelf_signature.id


    address = session.query(Address).filter_by(street=new_street, number=new_number, flat_number=new_flat_number,
                                               zip_code=new_zip_code, city=new_city, country=new_country).first()
    if address is None:
        operation_status, new_address_id = add_address(new_street, new_number, new_flat_number,new_zip_code, new_city, new_country)
    else:
        new_address_id = address.id

    publisher = session.query(Publisher).filter_by(publisher=new_publisher,
                                                   publication_year = new_publication_year,
                                                   address_id=new_address_id).first()
    if publisher is None:
        operation_status, id = add_publisher(new_publisher, new_publication_year, new_address_id)
        new_book.publisher_id = id
    else:
        new_book.publisher_id = publisher.id


    session.add(new_book)
    session.commit()

    # relation to author
    author = session.query(Author).filter_by(author_name=new_author_name, author_surname=new_author_surname).first()
    if author is None:
        operation_status, author_id = add_author(new_author_name, new_author_surname)
        new_author = session.query(Author).filter_by(id=author_id).first()
    new_author=author
    if author is None:
        raise ValueError(f" {new_author_name} {new_author_surname} was not added too the databse!")

    # relation to category
    category = session.query(Category).filter_by(category_name=new_category).first()
    if category is None:
        operation_status, category_id = add_category(category_name=new_category)
        new_category = session.query(Category).filter_by(id=category_id).first()
    new_category=category
    if category is None:
        raise ValueError(f"{new_category} was not added to the database")

    # relation to tag
    tag = session.query(Tag).filter_by(tag=new_tag).first()
    if tag is None:
        operation_status, tag_id = add_tag(tag_name=new_tag)
        new_tag = session.query(Tag).filter_by(id=tag_id).first()
    new_tag=tag
    if tag is None:
        raise ValueError(f"{new_tag} was not added to the database")

    new_book.authors.append(new_author)
    new_book.categories.append(new_category)
    new_book.tags.append(new_tag)

    session.commit()


# def add_book(title_name, authors, isbn_number, language_name,
#              shelf_signature_number, tag_name, indicated_publisher,  indicated_publication_year, indicated_street,
#              indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country,
#              indicated_category_name):
#
#     title = session.query(Title).filter_by(title=title_name).first()
#     if is_title_in_db(title_name)==False:
#         add_title(title_name)
#         print(f'Title: {title_name} was added to the database.')
#     else:
#         print(f'Title: {title_name} is already in the database.')
#     new_book = Book()
#     new_book.title=title
#
#     for indicated_author_name, indicated_author_surname in authors:
#         if is_author_in_db(indicated_author_name, indicated_author_surname)==False:
#             add_author(indicated_author_name, indicated_author_surname)
#             print(f'Author: {indicated_author_name} {indicated_author_surname} was added to the database.')
#         else:
#             print(f'Author: {indicated_author_name} {indicated_author_surname} is already in the database.')
#         author = session.query(Author).filter_by(author_name=indicated_author_name,
#                                                  author_surname=indicated_author_surname).first()
#         new_book.authors.append(author)
#
#     isbn_name = session.query(Isbn).filter_by(isbn_name=isbn_number).first()
#     if is_isbn_in_db(isbn_number)==False:
#         add_isbn(isbn_number)
#         print(f'Isbn: {isbn_number} was added to the database.')
#     else:
#         print(f'Isbn {isbn_number} already exists in database')
#     new_book.isbn_name=isbn_name
#
#     language = session.query(Language).filter_by(language=language_name).first()
#     if is_language_in_db(language_name)==False:
#         add_language(language_name)
#         print(f'Language: {language_name} was added to the database.')
#     else:
#         print(f'Language {language_name} already exists in database')
#     new_book.language=language
#
#     shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()
#     if is_shelf_signature_in_db(shelf_signature_number)==False:
#         add_shelf_signature(shelf_signature_number)
#         print(f'Shelf signature: {shelf_signature_number} was added to the database.')
#         shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()
#     else:
#         print(f'Shelf signature: {shelf_signature_number} already exists in database')
#     new_book.shelf_signature=shelf_signature
#
#     tag = session.query(Tag).filter_by(tag=tag_name).first()
#     if is_tag_in_db(tag_name)==False:
#         add_tag(tag_name)
#         print(f'Tag: {tag_name} was added to the database.')
#     else:
#         print('Tag: {tag_name} already exists in database')
#     new_book.tag=tag
#
#     publisher = session.query(Publisher).filter_by(publisher=indicated_publisher,
#                                                    publication_year=indicated_publication_year).first()
#     if is_publisher_in_db(indicated_publisher, indicated_publication_year)==False:
#         add_publisher(indicated_publisher, indicated_publication_year)
#         print(f'Publisher: {indicated_publisher} was added to the database.')
#     else:
#         print(f'Publisher: {indicated_publisher} with publication year {indicated_publication_year} already exists in database')
#     new_book.publisher=publisher
#
#     address = session.query(Publisher).filter_by(publisher=indicated_publisher,
#                                                  publication_year=indicated_publication_year).first()
#     if is_address_in_db(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city,
#                         indicated_country)==False:
#         add_address(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country)
#         print(f'Address: {indicated_street}, {indicated_number}, {indicated_flat_number}, {indicated_zip_code}, '
#               f'{indicated_city}, {indicated_country} was added to the database.')
#     else:
#         print(f'Address: {indicated_street}, {indicated_number}, {indicated_flat_number}, {indicated_zip_code}, '
#               f'{indicated_zip_code}, {indicated_city}, {indicated_country} already exists in database')
#     new_book.address=address
#
#     for category in indicated_category_name:
#         if is_category_in_db(indicated_category_name)==False:
#             add_category(indicated_category_name)
#             print(f'Category: {indicated_category_name} was added to the database.')
#         else:
#             print(f'Category: {indicated_category_name} already exists in database')
#         new_book.category=category
#
#     session.add(new_book)
#     session.commit()
#     _id = new_book.id
#     print(f'New book: {title_name}, {indicated_author_name} {indicated_author_surname}, {isbn_number}, {language_name}, '
#           f'{shelf_signature_number}, {tag_name},{indicated_category_name} was added with ID: {_id}')

def is_book_in_db(title_name, indicated_author_name, indicated_author_surname, isbn_number, language_name,
             shelf_signature_number,tag_name, indicated_publisher, indicated_publication_year,
             category_name):
    book = session.query(Book).filter_by(title=title_name, author_name=indicated_author_name,
                                               author_surname=indicated_author_surname, isbn=isbn_number,
                                               language=language_name, shelf_signature=shelf_signature_number,
                                         tag=tag_name, publisher=indicated_publisher,
                                         publication_year= indicated_publication_year, category=category_name).first()

    if book:
        _id=book.id
        print(f'ID: {_id}, Book: {title_name}, {indicated_author_name}, {indicated_author_surname}, '
              f'{isbn_number}, {language_name}, {shelf_signature_number}, {tag_name}, {indicated_publisher}, '
              f'{indicated_publication_year}, {category_name} is already in database.')
        return True
    return False

def get_books_list():
    books_list = session.query(Book).all()

    if books_list:
        print(f'Books list:')
        for book in books_list:
            _id = book.id
            print(f'ID: {_id}, Book: {book.title}, {book.author_name}, {book.author_surname}, {book.isbn}, '
                  f'{book.language}, {book.shelf_signature}, {book.tag}, {book.publisher}, {book.publication_year}, {category}')
        return books_list
    return OPER_GET_LIST_FAILED

def update_book(old_street, updated_street, old_number, updated_number, old_flat_number, updated_number_flat,
                    old_zip_code, updated_zip_code, old_city, updated_city, old_country, updated_country):
    address = session.query(Address).filter_by(street=old_street, number=old_number, flat_number=old_flat_number,
                                               zip_code=old_zip_code, city=old_city, country=old_country ).first()

    if address:
        address = Address(street=updated_street, number=updated_number, flat_number=updated_number_flat,
                          zip_code=updated_zip_code, city=updated_city, country=updated_country)
        _id = address.id
        session.commit()
        print(f'ID: {_id}, Address: {old_street} {old_number} {old_flat_number}, {old_zip_code},'
              f'{old_city}, {old_country} was updated to {updated_street} {updated_number}, '
              f'{updated_number_flat},{updated_zip_code}, {updated_city}, {updated_country}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_address(indicated_street, indicated_number, indicated_flat_number,
                    indicated_zip_code, indicated_city, indicated_country):
    address = session.query(Address).filter_by(street=indicated_street, number=indicated_number,
                                               flat_number=indicated_flat_number,zip_code=indicated_zip_code,
                                               city=indicated_city, country=indicated_country).first()

    if address:
        _id=address.id
        session.delete(address)
        session.commit()
        print(f'ID: {_id}, Address: {indicated_street} {indicated_number} {indicated_flat_number}, {indicated_zip_code},'
              f'{indicated_city}, {indicated_country} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS





