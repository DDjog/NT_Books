import logging
import src.logging_to_file
from src.operations.books_operations import add_book
from src.operations.title_operations import add_title
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

b=['FHow to solve your own murder','FKristen', 'FPerrin','F978-1-52943-007-3','Fenglish', '423112', 'Fmurder',
   'FQuercus', 'FViktoria Embankment', '42150','4211', '421EC4Y', 'FLondon', 'FGreat Britain', 4212024, 'Fnovel']

(new_title, new_author_name, new_author_surname, new_isbn, new_language, new_shelf_signature, new_tag,
new_publisher, new_street, new_number, new_flat_number, new_zip_code, new_city, new_country,
new_publication_year, new_category) = b

operation_status, book_id =add_book(new_title, new_author_name, new_author_surname,
new_isbn, new_language, new_shelf_signature, new_tag,
new_publisher, new_street, new_number, new_flat_number, new_zip_code, new_city, new_country,
new_publication_year, new_category)

if operation_status == OPER_ADD_SUCCEEDED:
   logging.info(f"New book:{new_title} {new_isbn} was added to the database")
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
   logging.warning(f'Book:{new_title} {new_isbn} exists already in the database')


