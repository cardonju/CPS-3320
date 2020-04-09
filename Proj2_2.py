import sqlalchemy as db
from sqlalchemy import create_engine

#trying to create an engine to connect to a database.  in this case the database for 
#CPS3740 class it requieres the database user information and password as well as the
#mysql port
engine = create_engine('mysql://cardonju:imc.kean.edu:3306/CPS3740')

connection = engine.connect()
metadata = db.MetaData()
customer = db.Table('customer', metadata, autoload=True, autoload_with=engine)

#print customer table columns
print(customer.columns.keys())
#print full table
print(repr(metadata.tables['customer']))