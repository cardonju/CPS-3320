import sqlalchemy as db
from sqlalchemy import create_engine

#trying to create an engine to connect to a database.  in this case the database  
#class it requieres the database user information and password as well as the
#mysql port
engine = create_engine('')

connection = engine.connect()
metadata = db.MetaData()
customer = db.Table('customer', metadata, autoload=True, autoload_with=engine)

#print customer table columns
print(customer.columns.keys())
#print full table
print(repr(metadata.tables['customer']))