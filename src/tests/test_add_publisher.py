from src.database.db import session
from src.database.models import Address
from src.operations.publisher_operations  import add_publisher
from src.operations.address_operations import add_address

a = ['Warsaw Street', '10', '5', '00-123',
            'London', 'Great Britain']
add_address({a})

address = session.query(Address).filter_by(
    street='Warsaw Street',
    number= '10',
    flat_number='5',
    zip_code='00-123',
    city='London',
    country='Great Britain'
).first()
if address:
    global p
    p = ['AXA', '2009', address.id]
    add_publisher({p})
    print(f'{p} was added to the database')
else:
    print(f'{p} was not found in the database')
