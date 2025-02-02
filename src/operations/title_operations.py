
from src.database.models import Title
from src.database.db import session
from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, \
    OPER_GET_LIST_FAILED, OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_DELETE_SUCCEEDED


def add_title(title_name):
    title = session.query(Title).filter_by(title=title_name).first()

    if not title:
        title = Title(title=title_name)
        session.add(title)
        session.commit()
        print(f'Title: {title_name} was added.')
        return OPER_ADD_SUCCEEDED
    return OPER_ADD_FAILED_DATA_EXISTS

def is_title_in_db(title_name):
    title = session.query(Title).filter_by(title=title_name).first()

    if title:
        _id = title.id
        print(f'ID: {_id}, Title: {title_name}')
        return True
    return False

def get_titles_list():
    titles_list = session.query(Title).all()

    if titles_list:
        print(f'Titles list:')
        for title in titles_list:
            _id = title.id
            print(f'ID: {_id}, Title: {title.title}')
        return titles_list
    return OPER_GET_LIST_FAILED

def update_title(old_title_name, updated_title_name):
    title = session.query(Title).filter_by(title=old_title_name).first()

    if title:
        _id=title.id
        title.language = updated_title_name
        session.commit()
        print(f'ID: {_id}, Title: {old_title_name} was updated to {updated_title_name}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_title(title_name):
    title = session.query(Title).filter_by(title=title_name).first()

    if title:
        _id=title.id
        session.delete(title)
        session.commit()
        print(f'ID: {title.id}, Title: {title_name} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS


