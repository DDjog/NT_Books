
from src.database.models import ShelfSignature
from src.database.db import session

def add_shelf_signature(shelf_signature_number):
    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number)

    if not shelf_signature:
        shelf_signature = ShelfSignature(shelf_signature=shelf_signature_number)
        session.add(shelf_signature_number)
        session.commit()
        print(f'Shelf signature: {shelf_signature_number} was added.')
    else:
        print(f'Shelf signature: {shelf_signature_number} already exists.')

def is_shelf_signature_in_db(shelf_signature_number):
    shelf_signature = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature_number)

    if shelf_signature:
        return True
    return False

