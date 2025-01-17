
from src.database.models import Publisher
from src.database.db import session

def add_publisher(indicated_publisher, indicated_publication_year, indicated_address_id):
    publisher = session.query(Publisher).filter_by(publisher=indicated_publisher, publication_year=indicated_publication_year, address_id=indicated_address_id)

    if not publisher:
        publisher = Publisher(publisher=indicated_publisher, publication_year=indicated_publication_year, address_id=indicated_address_id)
        session.add(publisher)
        session.commit()
        print(f'Publisher: {indicated_publisher}, publication year: {indicated_publication_year} were added.')
    else:
        print(f'Publisher: {indicated_publisher} already exists.')

def is_publisher_in_db(indicated_publisher, indicated_publication_year):
    publisher = session.query(Publisher).filter_by(publisher=indicated_publisher, publication_year=indicated_publication_year)

    if publisher:
        print(f'Publisher: {indicated_publisher} is in a database.')
        return True
    return False
