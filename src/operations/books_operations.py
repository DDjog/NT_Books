from src.database.models import (Book, Title, Isbn, Language, Cover_page, ShelfSignature, Author,
                    Tag, Publisher, Category)
from src.database.db import session


def add_book(title_name, indicated_author_name, indicated_author_surname, new_isbn, new_language, new_cover_page, new_shelf_signature,
             new_tag_list, new_publisher, new_publication_year, new_category_name):

    # title = Title(title=title_name)
    #
    # authors = []
    # for author in authors_list:
    #     author = Author(author_name=nauthor['name'], author_surname=new_author['surname'])
    #     authors.append(new_author)
    #
    # isbn = Isbn(isbn_name=new_isbn)
    # language = Language(language=new_language)
    # cover_page = Cover_page(cover_page=new_cover_page)
    # shelf_signature = ShelfSignature(shelf_signature=new_shelf_signature)
    #
    # tags = []
    # for new_tag in new_tag_list:
    #     new_tag = Tag(tag=new_tag)
    #     tags.append(new_tag)
    #
    # publisher = Publisher(publisher=new_publisher, publication_year=new_publication_year)
    #
    # category = Category(category_name=new_category_name)
    #
    # new_book = Book(
    #     title=new_title,
    #     author_name=new_author_list,
    #     isbn_name=new_isbn,
    #     language=new_language,
    #     cover_page=new_cover_page,
    #     shelf_signature=new_shelf_signature,
    #     tags=new_tag_list,
    #     publisher=new_publisher,
    #     cathegory_name=new_category_name
    # )
    # session.add(new_book)
    # session.commit()
    # print(f'New book {new_book} was added.')
    pass

def add_shelf_signature(new_shelf_signature):
    shelf_signatures_list = [ShelfSignature.shelf_signature for shelf_signature in session.query(ShelfSignature).all()]
    if new_shelf_signature not in shelf_signatures_list:
        shelf_signature = ShelfSignature(shelf_signature=new_shelf_signature)
        session.add(new_shelf_signature)
        session.commit()
        print(f'New shelf signature {new_shelf_signature} was added.')
    else:
        print(f'New shelf signature {new_shelf_signature} already exists.')


