from src.constans import OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_UPDATE_SUCCEEDED, \
    OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS
from src.database.models import Language
from src.database.db import session

def add_language(language_name):
    language = session.query(Language).filter_by(language=language_name).first()

    if not language:
        language = Language(language=language_name)
        session.add(language)
        session.commit()
        return OPER_ADD_SUCCEEDED, language.id
    return OPER_ADD_FAILED_DATA_EXISTS, language.id

def is_language_in_db(language_name):
    language = session.query(Language).filter_by(language=language_name).first()

    if language:
        _id = language.id
        print(f'ID: {_id}, Language: {language_name}')
        return True
    return False

def get_languages_list():
    languages_list = session.query(Language).all()

    if languages_list:
        print(f'Languages list:')
        for language in languages_list:
            _id = language.id
            print(f'ID: {_id}, Language: {language.language}')
        return languages_list
    return OPER_GET_LIST_FAILED

def update_language(old_language_name, new_language_name):
    language = session.query(Language).filter_by(language=old_language_name).first()

    if language:
        _id = language.id
        language.language = new_language_name
        session.commit()
        print(f'ID: {_id}, Language: {old_language_name} was updated to {new_language_name}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_language(language_name):
    language = session.query(Language).filter_by(language=language_name).first()

    if language:
        _id=language.id
        session.delete(language)
        session.commit()
        print(f'ID: {_id}, Language: {language_name} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS


