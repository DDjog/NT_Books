
from src.database.models import ShelfSignature
from src.database.db import session
from src.constans import OPER_ADD_FAILED_DATA_EXISTS, OPER_ADD_SUCCEEDED, \
    OPER_GET_LIST_FAILED, OPER_UPDATE_SUCCEEDED, OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_DELETE_SUCCEEDED, \
    OPER_DELETE_FAILED_DATA_NOT_EXISTS


def add_shelf_signature(shelf_signature_number):
    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number)

    if not shelf_signature:
        shelf_signature = ShelfSignature(shelf_signature=shelf_signature_number)
        session.add(shelf_signature)
        session.commit()
        print(f'Shelf signature: {shelf_signature_number} was added.')
        return OPER_ADD_SUCCEEDED
    return OPER_ADD_FAILED_DATA_EXISTS

def is_shelf_signature_in_db(shelf_signature_number):
    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number)

    if shelf_signature:
        return True
    return False

def get_shelf_signatures_list():
    shelf_signatures_list = session.query(ShelfSignature).all()

    if shelf_signatures_list:
        print(f'Shelf signatures list:')
        for shelf_signature in shelf_signatures_list:
            _id = shelf_signature.id
            print(f'ID: {_id}, Shelf signature: {shelf_signature.shelf_signature}')
        return shelf_signatures_list
    return OPER_GET_LIST_FAILED

def update_shelf_signature(old_shelf_signature, new_shelf_signature):
    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=old_shelf_signature).first()

    if shelf_signature:
        _id = shelf_signature.id
        shelf_signature.shelf_signature = new_shelf_signature
        session.commit()
        print(f'ID: {_id}, shelf signature: {old_shelf_signature} was updated to {new_shelf_signature}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_shelf_signature(shelf_signature_number):
    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number).first()

    if shelf_signature:
        _id=shelf_signature.id
        session.delete(shelf_signature)
        session.commit()
        print(f'ID: {_id}, shelf signature: {shelf_signature_number} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS