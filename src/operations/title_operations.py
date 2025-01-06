
from src.database.models import Title
from src.database.db import session

def add_title(title_name):
    title = session.query(Title).filter_by(title=title_name).first()

    if not title:
        title = Title(title=title_name)
        session.add(title)
        session.commit()
        print(f'Title {title_name} was added.')
    else:
        print(f'Title {title_name} already exists.')

def get_title(title_name):
    title = session.query(Title).filter_by(title=title_name).first()

    if title:
        print(f'Title: {title_name}, ID: {title.id}')
    else:
        print(f':Title {title_name} was not found')

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

def update_title(old_title_name, updated_title_name):
    title = session.query(Title).filter_by(title=old_title_name).first()

    if title:
        title.language = updated_title_name
        session.commit()
        print(f'Title: {id} {old_title_name} was updated to {updated_title_name}.')
    else:
        print(f'Title {old_title_name} was not found.')

def delete_title(title_name):
    title = session.query(Title).filter_by(title=title_name).first()

    if title:
        _id=title.id
        session.delete(title)
        session.commit()
        print(f'Title: {_id} {title_name} was deleted.')
    else:
        print(f'Title {title_name} was not found.')


