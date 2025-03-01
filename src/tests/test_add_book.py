from src.operations.books_operations import add_book
from src.operations.title_operations import add_title
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS



operation_status, book_id =add_book('FHow to solve your own murder',
      'FKristen',  'FPerrin',
         'F978-1-52943-007-3','Fenglish', '423112', 'Fmurder',
         'FQuercus', 'FViktoria Embankment', '42150',
    '4211', '421EC4Y', 'FLondon', 'FGreat Britain',
         4212024, 'Fnovel' )

if operation_status == OPER_ADD_SUCCEEDED:
   print(f"New book was added to the database")
elif operation_status == OPER_ADD_FAILED_DATA_EXISTS:
   print(f'New book exists already in the database')


# r, title_id = add_title('AHow to solve your own murder')
# print(f'{r}, {title_id}')
#
# add_book(title_id,  )
