from models import (Book, Title, Isbn, Language, Cover_page, ShelfSignature, Author,
                    Tag, Publisher, Category)
from db import session


def add_book(new_title, new_author_list, new_isbn, new_language, new_cover_page, new_shelf_signature,
             new_tag_list, new_publisher, new_publication_year, new_category_name):

    title = Title(title=new_title)

    authors = []
    for new_author in new_author_list:
        new_author = Author(author_name=new_author['name'], author_surname=new_author['surname'])
        authors.append(new_author)

    isbn = Isbn(isbn_name=new_isbn)
    language = Language(language=new_language)
    cover_page = Cover_page(cover_page=new_cover_page)
    shelf_signature = ShelfSignature(shelf_signature=new_shelf_signature)

    tags = []
    for new_tag in new_tag_list:
        new_tag = Tag(tag=new_tag)
        tags.append(new_tag)

    publisher = Publisher(publisher=new_publisher, publication_year=new_publication_year)

    category = Category(category_name=new_category_name)

    new_book = Book(
        title=new_title,
        author_name=new_author_list,
        isbn_name=new_isbn,
        language=new_language,
        cover_page=new_cover_page,
        shelf_signature=new_shelf_signature,
        tags=new_tag_list,
        publisher=new_publisher,
        cathegory_name=new_category_name
    )
    session.add(new_book)
    session.commit()



