
from src.database.models import Publisher
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, \
    OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_NOT_EXISTS, OPER_ADD_SUCCEEDED


def add_publisher(indicated_publisher, indicated_publication_year, indicated_address_id):
    publisher = session.query(Publisher).filter_by(publisher=indicated_publisher, publication_year=indicated_publication_year, address_id=indicated_address_id).first()

    if not publisher:
        publisher = Publisher(publisher=indicated_publisher, publication_year=indicated_publication_year, address_id=indicated_address_id)
        session.add(publisher)
        session.commit()
        return OPER_ADD_SUCCEEDED, publisher.id
    return OPER_ADD_FAILED_DATA_EXISTS, publisher.id

def is_publisher_in_db(indicated_publisher, indicated_publication_year):
    publisher = session.query(Publisher).filter_by(publisher=indicated_publisher, publication_year=indicated_publication_year)

    if publisher:
        print(f'Publisher: {indicated_publisher} is in a database.')
        return True
    return False

def get_publishers_list():
    publishers_list = session.query(Publisher).all()

    if publishers_list:
        print(f'Publishers list:')
        for publisher in publishers_list:
            _id = publisher.id
            session.commit()
            print(f'ID: {_id}, Publisher: {publisher.publisher}')
        return publishers_list
    return OPER_GET_LIST_FAILED

def update_publisher(old_publisher_name, updated_publisher_name):
    publisher = session.query(Publisher).filter_by(publisher=old_publisher_name).first()

    if publisher:
        _id=publisher.id
        publisher.publisher = updated_publisher_name
        session.commit()
        print(f'ID: {_id}, Publisher: {old_publisher_name} was updated to {updated_publisher_name}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_publisher(publisher_name):
    publisher = session.query(Publisher).filter_by(publisher=publisher_name).first()

    if publisher:
        _id=publisher.id
        session.delete(publisher)
        session.commit()
        print(f'ID: {publisher.id}, Publisher: {publisher} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS
