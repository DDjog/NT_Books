
from src.database.models import Title
from src.database.db import session

def add_title(new_title):
    title = session.query(Title).filter_by(title=new_title).first()

    if not title:
        title = Title(title=new_title)
        session.add(title)
        session.commit()
        print(f'Title {new_title} was added.')
    else:
        print(f'Title {new_title} already exists.')

def get_title(title):
    title = session.query(Title).filter_by(title=title).first()

    if title:
        print(f'Title: {title}, ID: {title.id}')
    else:
        print(f':Title {title} was not found')

def get_titles_list():
    titles_list = session.query(Title).all()

    if titles_list:
        print(f'Titles list:')
        for title in titles_list:
            print(f'ID: {Title.id}, Title: {Title.title}')
        return titles_list
    else:
        print('Titles list is empty')
        return None

def update_title(title, updated_title):
    title = session.query(Title).filter_by(title=title).first()

    if title:
        title.language = updated_title
        session.commit()
        print(f'Title: {id} {title} was updated to {updated_title}.')
    else:
        print(f'Title {title} was not found.')

def delete_title(title):
    title = session.query(Title).filter_by(title=title).first()

    if title:
        _id=title.id
        session.delete(title)
        session.commit()
        print(f'Title: {_id} {title} was deleted.')
    else:
        print(f'Title {title} was not found.')


