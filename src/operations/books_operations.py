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
from src.database.models import Book, Address, Author, Title, Isbn, Language, ShelfSignature, Tag, Publisher, Category
from src.constans import (OPER_DELETE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS , OPER_DELETE_SUCCEEDED, OPER_UPDATE_SUCCEEDED, \
    OPER_ADD_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS, OPER_UPDATE_FAILED_DATA_NOT_EXISTS,
                          OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_GET_LIST_FAILED)


def add_book(new_title, new_author_name, new_author_surname, new_isbn, new_language,
             new_shelf_signature, new_tag, new_publisher,  new_street, new_number, new_flat_number, new_zip_code,
             new_city, new_country, new_publication_year, new_category):

    new_book = Book()

    title = session.query(Title).filter_by(title=new_title).first()
    if not title.id:
        add_title(title.id)
    new_book.title=new_title

    # for author in authors:
    #     author = session.query(Author).filter_by(author_name=new_author_name,
    #                                              author_surname=new_author_surname).first()
    #     if not author.id:
    #         add_author(new_author_name, new_author_surname)
    #     new_book.authors.append(author)

    isbn_name = session.query(Isbn).filter_by(isbn_name=new_isbn).first()
    if not isbn_name.id:
        add_isbn(new_isbn)
    new_book.isbn_name=new_isbn

    language = session.query(Language).filter_by(language=new_language).first()
    if not language.id:
        add_language(new_language)
    new_book.language=new_language

    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=new_shelf_signature).first()
    if not shelf_signature.id:
        add_shelf_signature(new_shelf_signature)
    new_book.shelf_signature=new_shelf_signature

    tag = session.query(Tag).filter_by(tag=new_tag).first()
    if not tag.id:
        add_tag(new_tag)
    new_book.tag=new_tag

    publisher = session.query(Publisher).filter_by(publisher=new_publisher,
                                                   publication_year = new_publication_year).first()
    if not publisher.id:
        add_publisher(new_publisher)
    new_book.publisher=new_publisher

    # address = session.query(Address).filter_by(id=new_address.id).first()
    # if not address.id:
    #     add_address(new_street, new_number, new_flat_number, new_zip_code, new_city, new_country)
    # new_book.address=new_address

    for category in categories:
        category = session.query(Category).filter_by(category_name=new_category)
        if not category.id:
            add_category(new_category)
        new_book.category=new_category

    session.add(new_book)
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





