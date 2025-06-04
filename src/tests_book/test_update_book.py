import logging
import src.logging_to_file
from src.operations.books_operations import update_book
from src.constans import OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_EXISTS

b = ['FHow to solve your own murder', 'GHow to solve your own murder','FKristen', 'GKristen', 'FPerrin', 'GPerrin',
         'F978-1-52943-007-3','G978-1-52943-007-3', 'Fenglish', 'Genglish', '423112','523112','Fmurder', 'Gmurder',
         'FQuercus', 'GQuercus', 'FViktoria Embankment', 'GViktoria Embankment', '42150', '442150', '4211', '421EC4Y',
     '0356', '40356', 'FLondon',  'GLondon', 'FGreat Britain', 'GGreat Britain', '2024', '42024', 'Fnovel', 'Gnovel']

(old_title, new_title, old_author_name, new_author_name, old_author_surname, new_author_surname, old_isbn,
new_isbn, old_language, new_language, old_shelf_signature, new_shelf_signature, old_tag, new_tag,
old_publisher, new_publisher, old_street, new_street, old_number, new_number, old_flat_number, new_flat_number,
old_zip_code, new_zip_code, old_city, new_city, old_country, new_country, old_publication_year,
new_publication_year, old_category, new_category) = b

operation_status, book_id= update_book (old_title, new_title, old_author_name, new_author_name, old_author_surname, new_author_surname, old_isbn,
            new_isbn, old_language, new_language, old_shelf_signature, new_shelf_signature, old_tag, new_tag,
            old_publisher, new_publisher, old_street, new_street, old_number, new_number, old_flat_number, new_flat_number,
            old_zip_code, new_zip_code, old_city, new_city, old_country, new_country, old_publication_year,
            new_publication_year, old_category, new_category)
if operation_status == OPER_UPDATE_SUCCEEDED:
    logging.info(f'Book: {b} is in the database')
elif operation_status == OPER_UPDATE_FAILED_DATA_EXISTS:
    logging.warning(f'Book: {b} is not in the database')
