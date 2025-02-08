from src.database.models import Address
from src.database.db import session
from src.constans import (OPER_ADD_SUCCEEDED, OPER_ADD_FAILED_DATA_EXISTS, OPER_GET_LIST_FAILED, OPER_UPDATE_SUCCEEDED,
                          OPER_UPDATE_FAILED_DATA_NOT_EXISTS, OPER_DELETE_SUCCEEDED, OPER_DELETE_FAILED_DATA_NOT_EXISTS)


def add_address(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code,
                indicated_city, indicated_country):
    address = session.query(Address).filter_by(street=indicated_street, number= indicated_number,
                                               flat_number= indicated_flat_number, zip_code=indicated_zip_code,
                                               city=indicated_city, country=indicated_country).first()

    if not address:
        address = Address(street=indicated_street, number=indicated_number, flat_number=indicated_flat_number,
                          zip_code=indicated_zip_code, city=indicated_city, country=indicated_country)
        session.add(address)
        session.commit()
        return OPER_ADD_SUCCEEDED, address.id
    return OPER_ADD_FAILED_DATA_EXISTS, address.id

def is_address_in_db(indicated_street, indicated_number, indicated_flat_number, indicated_zip_code,
                     indicated_city, indicated_country):
    address = session.query(Address).filter_by(street=indicated_street, number=indicated_number,
                                               flat_number=indicated_flat_number, zip_code=indicated_zip_code,
                                               city=indicated_city, country=indicated_country).first()

    if address:
        _id=address.id
        print(f'ID: {_id}, Address: {indicated_street} {indicated_number} {indicated_flat_number} '
              f'{indicated_zip_code} {indicated_city} {indicated_country} is already in database.')
        return True
    return False

def get_addresses_list():
    addresses_list = session.query(Address).all()

    if addresses_list:
        print(f'Addresses list:')
        for address in addresses_list:
            _id = address.id
            print(f'ID: {_id}, Address: {address.street}, {address.number}, {address.flat_number}, {address.zip_code}, '
                  f'{address.city}, {address.country}')
        return addresses_list
    return OPER_GET_LIST_FAILED

def update_address(old_street, updated_street, old_number, updated_number, old_flat_number, updated_number_flat,
                    old_zip_code, updated_zip_code, old_city, updated_city, old_country, updated_country):
    address = session.query(Address).filter_by(street=old_street, number=old_number, flat_number=old_flat_number,
                                               zip_code=old_zip_code, city=old_city, country=old_country ).first()

    if address:
        address = Address(street=updated_street, number=updated_number, flat_number=updated_number_flat,
                          zip_code=updated_zip_code, city=updated_city, country=updated_country)
        _id = address.id
        session.commit()
        print(f'ID: {_id}, Address: {old_street} {old_number} {old_flat_number}, {old_zip_code},'
              f'{old_city}, {old_country} was updated to {updated_street} {updated_number}, '
              f'{updated_number_flat},{updated_zip_code}, {updated_city}, {updated_country}.')
        return OPER_UPDATE_SUCCEEDED
    return OPER_UPDATE_FAILED_DATA_NOT_EXISTS

def delete_address(indicated_street, indicated_number, indicated_flat_number,
                    indicated_zip_code, indicated_city, indicated_country):
    address = session.query(Address).filter_by(street=indicated_street, number=indicated_number,
                                               flat_number=indicated_flat_number,zip_code=indicated_zip_code,
                                               city=indicated_city, country=indicated_country).first()

    if address:
        _id=address.id
        session.delete(address)
        session.commit()
        print(f'ID: {_id}, Address: {indicated_street} {indicated_number} {indicated_flat_number}, {indicated_zip_code},'
              f'{indicated_city}, {indicated_country} was deleted.')
        return OPER_DELETE_SUCCEEDED
    return OPER_DELETE_FAILED_DATA_NOT_EXISTS
