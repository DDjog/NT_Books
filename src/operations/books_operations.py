
from src.operations.address_operations import is_address_in_db, add_address
from src.operations.author_operations import is_author_in_db, add_author
from src.operations.category_operations import is_category_in_db, add_category
from src.operations.language_operations import is_language_in_db, add_language
from src.operations.publisher_operations import is_publisher_in_db, add_publisher
from src.operations.title_operations import is_title_in_db, add_title
from src.operations.isbn_operations import is_isbn_in_db, add_isbn
from src.operations.shelf_signature_operations import is_shelf_signature_in_db, add_shelf_signature
from src.operations.tag_operations import is_tag_in_db, add_tag


def add_book(title_name, indicated_author_name, indicated_author_surname, isbn_number, language_name, cover_page_name, shelf_signature_number,
             tag_name, indicated_publisher, indicated_publication_year, indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country, category_name):

    if is_title_in_db(title_name)==False:
        add_title(title_name)
    else:
        print(f'Title: {title_name} exists already in database')

    if is_author_in_db(indicated_author_name, indicated_author_surname)==False:
        add_author(indicated_author_name, indicated_author_surname)
    else:
        print(f'Author {indicated_author_name} {indicated_author_surname} already exists in database')

    if is_isbn_in_db(isbn_number)==False:
        add_isbn(isbn_number)
    else:
        print(f'Isbn {isbn_number} already exists in database')

    if is_language_in_db(language_name)==False:
        add_language(language_name)
    else:
        print(f'Isbn {language_name} already exists in database')

    if is_shelf_signature_in_db(shelf_signature_number)==False:
        add_shelf_signature(shelf_signature_number)
    else:
        print(f'Shelf signature {shelf_signature_number} already exists in database')

    if is_tag_in_db(tag_name)==False:
        add_tag(tag_name)
    else:
        print('Tag {tag_name} already exists in database')

    if is_publisher_in_db(indicated_publisher, indicated_publication_year)==False:
        add_publisher(indicated_publisher, indicated_publication_year)
    else:
        print(f'Publisher {indicated_publisher} already exists in database')

    if is_address_in_db(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country)==False:
        add_address(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country)
    else:
        print('Address {tag_name} already exists in database')

    if is_category_in_db(category_name)==False:
        add_category(category_name)
    else:
        print(f'Category {category_name} already exists in database')






