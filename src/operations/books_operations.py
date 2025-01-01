from src.database.models import (Book, Title, Isbn, Language, Cover_page, ShelfSignature, Author,
                    Tag, Publisher, Category)
from src.database.db import session


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
    print(f'New book {new_book} was added.')

def add_language(new_language):
    languages_list = [language.language for language in session.query(Language).all()]

    if new_language not in languages_list:
        language = Language(language=new_language)
        session.add(new_language)
        session.commit()
        print(f'New language {new_language} was added.')
    else:
        print(f'New language {new_language} already exists.')

def add_tag(new_tag):
    tags_list = [tag.tag for tag in session.query(Tag).all()]
    if new_tag not in tags_list:
        tag = Tag(tag=new_tag)
        session.add(new_tag)
        session.commit()
        print(f'New tag {new_tag} was added.')
    else:
        print(f'New tag {new_tag} already exists.')

def add_shelf_signature(new_shelf_signature):
    shelf_signatures_list = [ShelfSignature.shelf_signature for shelf_signature in session.query(ShelfSignature).all()]
    if new_shelf_signature not in shelf_signatures_list:
        shelf_signature = ShelfSignature(shelf_signature=new_shelf_signature)
        session.add(new_shelf_signature)
        session.commit()
        print(f'New shelf signature {new_shelf_signature} was added.')
    else:
        print(f'New shelf signature {new_shelf_signature} already exists.')


