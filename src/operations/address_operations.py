from src.database.models import Address
from src.database.db import session

def add_address(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country):
    address = session.query(Address).filter_by(street=indicated_street, number= indicated_number, flat_number= indicated_flat_number, zip_code=indicated_zip_code, city=indicated_city, country=indicated_country).first()

    if not address:
        address = Address(street=indicated_street, number=indicated_number, flat_number=indicated_flat_number, zip_code=indicated_zip_code, city=indicated_city, country=indicated_country)
        session.add(address)
        session.commit()
        print(f'Address: {indicated_street} {indicated_number} {indicated_flat_number} {indicated_zip_code} {indicated_city} {indicated_country} was added.')
    else:
        print(f'Address already exists in database.')

def is_address_in_db(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code, indicated_city, indicated_country):
    address = session.query(Address).filter_by(street=indicated_street, number=indicated_number, flat_number=indicated_flat_number, zip_code=indicated_zip_code, city=indicated_city, country=indicated_country).first()

    if address:
        print(f'Address: {indicated_street} {indicated_number} {indicated_flat_number} {indicated_zip_code} {indicated_city} {indicated_country} is already in database')
        return True
    print('Isbn number incorrect')
    return False