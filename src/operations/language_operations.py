
from src.database.models import Language
from src.database.db import session

def add_language(new_language):
    language = session.query(Language).filter_by(language=new_language).first()

    if not language:
        language = Language(language=new_language)
        session.add(language)
        session.commit()
        print(f'Language {new_language} was added.')
    else:
        print(f'Language {new_language} already exists.')

def get_language(lang):
    language = session.query(Language).filter_by(language=lang).first()

    if language:
        print(f'Language: {lang}, ID: {language.id}')
    else:
        print(f':Language {language} was not found')

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

def update_language(language, updated_language):
    language = session.query(Language).filter_by(language=language).first()

    if language:
        language.language = updated_language
        session.commit()
        print(f'Language: {id} {language} was updated to {updated_language}.')
    else:
        print(f'Language {language} was not found.')

def delete_language(language):
    language = session.query(Language).filter_by(language=language).first()

    if language:
        _id=language.id
        session.delete(language)
        session.commit()
        print(f'Language: {_id} {language} was deleted.')
    else:
        print(f'Language {language} was not found.')


