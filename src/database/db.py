from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

PG_URL = "postgresql+psycopg2://postgres:secret@localhost:5432/Books"
engine = create_engine(PG_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session=Session()


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# import sqlite3
#
# conn = sqlite3.connect('Books.db')
#
# conn.execute('''CREATE TABLE BOOKS
# (ID INT PRIMARY KEY NOT NULL,
# TITLE TEXT NOT NULL,
# ISBN STRING NOT NULL,
# AUTHOR STRING NOT NULL,
# TAG STRING NOT NULL,
# PUBLISHER_ID INT NOT NULL,
# PUBLISHER STRING NOT NULL,
# CATEGORY_ID INT NOT NULL,
# CATEGORY STRING NOT NULL,
# SHELF_SIGNATURE_ID INT NOT NULL,
# SHELF_SIGNATURE INT NOT NULL);''')
#
# conn.execute("INSERT INTO BOOKS (ID, TITLE, ISBN, AUTHOR, TAG, \
# PUBLISHER_ID, PUBLISHER, CATEGORY_ID, CATEGORY, SHELF_SIGNATURE_ID, SHELF_SIGNATURE)\
#              VALUES (1, 'The Pillars of the Earth',9788383613932, 'Ken Follet', \
#              'history', 1, 'Albatros', '1', 'historyczna', 1, 1  )")
# conn.execute("INSERT INTO BOOKS (ID, TITLE, ISBN, AUTHOR, TAG, \
# PUBLISHER_ID, PUBLISHER, CATEGORY_ID, CATEGORY, SHELF_SIGNATURE_ID, SHELF_SIGNATURE)\
#              VALUES (2, 'Niepokorni',9788381437653, 'Vincent Viktor Severski', \
#              'spy', 2, '`Czarna Owca`', 'kryminał', 2, 2, 2  )")
# conn.execute("INSERT INTO BOOKS (ID, TITLE, ISBN, AUTHOR, TAG, \
# PUBLISHER_ID, PUBLISHER, CATEGORY_ID, CATEGORY, SHELF_SIGNATURE_ID, SHELF_SIGNATURE)\
#              VALUES (3, 'Bezcenny',9788383183404, 'Zygmunt Miłoszewski', \
#              'thriller', 3, 'WAB', 'przygpdpwa' , 3, 3, 3  )")
#
# cursor = conn.execute('SELECT id, title, isbn, author, tag, \
#                       publisher_id, publisher, category_id, category, shelf_signature_id, \
#                       shelf_signature from BOOKS')
# for row in cursor:
#     print('ID = ', row[0])
#     print('TITLE = ', row[1])
#     print('ISBN = ', row[2])
#     print('AUTHOR = ', row[3])
#     print('TAG = ', row[4])
#     print('PUBLISHER_ID = ', row[5])
#     print('PUBLISHER = ', row[6])
#     print('CATEGORY_ID = ', row[7])
#     print('CATEGORY = ', row[8])
#     print('SHELF_SIGNATURE_ID = ', row[9])
#     print('SHELF_SIGNATURE = ', row[10])
#     print('')
#     print('*************')
#     print('')
#
# conn.commit()
#
# conn.close()
#
