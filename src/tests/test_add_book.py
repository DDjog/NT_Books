from src.operations.books_operations import add_book
from src.operations.title_operations import add_title
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS

#ad = ['How to solve your own murder', [('Kristen',  'Perrin')],
#         '978-1-52943-007-3','english', '12', 'murder',
#         'AQuercus',2024, 'AViktoria Embankment', '50',
#    '1', 'EC4Y', 'London', 'Great Britain',
#         'novel']

# a = add_book(*ad)

add_book('DHow to solve your own murder',
      'DKristen',  'DPerrin',
         'D978-1-52943-007-3','Denglish', '2112', 'Dmurder',
         'DQuercus', 'DViktoria Embankment', '2150',
    '211', '21EC4Y', 'DLondon', 'DGreat Britain',
         212024, 'Dnovel' )

#if a == OPER_ADD_SUCCEEDED:
#    print(f"{a} was added to the database")
#elif a == OPER_ADD_FAILED_DATA_EXISTS:
#    print(f'{a} exists already in the database')


# r, title_id = add_title('AHow to solve your own murder')
# print(f'{r}, {title_id}')
#
# add_book(title_id,  )
