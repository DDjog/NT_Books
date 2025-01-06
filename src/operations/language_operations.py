
from src.database.models import Language
from src.database.db import session

def add_language(language_name):
    language = session.query(Language).filter_by(language=language_name).first()

    if not language:
        language = Language(language=language_name)
        session.add(language)
        session.commit()
        print(f'Language {language_name} was added.')
    else:
        print(f'Language {language_name} already exists.')

def find_language(language_name):
    language = session.query(Language).filter_by(language=language_name).first()

    if language:
        print(f'Language: {language_name}, ID: {language.id}')
    else:
        print(f':Language {language_name} was not found')

def get_languages_list():
    languages_list = session.query(Language).all()

    if languages_list:
        print(f'Languages list:')
        for language in languages_list:
            print(f'ID: {language.id}, Language: {language.language}')
        return languages_list
    else:
        print('Languages list is empty')
        return None

def update_language(old_language_name, new_language_name):
    language = session.query(Language).filter_by(language=old_language_name).first()

    if language:
        language.language = new_language_name
        session.commit()
        print(f'Language: {id} {old_language_name} was updated to {new_language_name}.')
    else:
        print(f'Language {old_language_name} was not found.')

def delete_language(language_name):
    language = session.query(Language).filter_by(language=language_name).first()

    if language:
        _id=language.id
        session.delete(language)
        session.commit()
        print(f'Language: {_id} {language_name} was deleted.')
    else:
        print(f'Language {language_name} was not found.')


