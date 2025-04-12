import logging
import src.logging_to_file
from src.constans import OPER_ADD_SUCCEEDED
from src.database.db import session
from src.database.models import Address
from src.operations.publisher_operations  import add_publisher
from src.operations.address_operations import add_address


a = ['AWarsaw Street', '110', '15', '100-123',
            'ALondon', 'AGreat Britain']
street, number, flat_number, zip_code, city, country = a
address = session.query(Address).filter_by(
    street=street,
    number= number,
    flat_number=flat_number,
    zip_code=zip_code,
    city=city,
    country=country
).first()
if not address:
    operation_status, address_id = add_address(street, number, flat_number, zip_code, city, country)
else:
    address_id=address.id

p = ['AXA', '2009', address_id]
publisher_name, publication_year, address_id = p
operation_status, address_id = add_publisher(publisher_name, publication_year, address_id)
if operation_status == OPER_ADD_SUCCEEDED:
    logging.info(f'{p} was added to the database')
else:
    logging.warning(f'{p} was not found in the database')
