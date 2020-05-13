# Day 2 in class

# Imports
import os
from dotenv import load_dotenv
import psycopg2

# # Save credentials
# db_name='ktvhavcy' 
# db_user='ktvhavcy'
# db_pwd='a97TPJBPVK7eFJdoUozeotpqG9jmItjE' 
# db_host='rajje.db.elephantsql.com'

# Load contents of .env file which holds credentials.
load_dotenv()

# Use environment variables to load credentials, so other peopole can access the files and not see the credentials
db_name = os.getenv('db_name', default= 'OOPS')
db_user = os.getenv('db_user', default= 'OOPS')
db_pwd = os.getenv('db_pwd', default= 'OOPS')
db_host = os.getenv('db_host', default= 'OOPS')

# Put environmental variables in a hidden file called dotenv. The os will pull from this and fill in the credentials


# Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=db_name, user=db_user,
                        password=db_pwd, host=db_host)
print(type(connection))

# A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print(type(cursor))

# An example query
cursor.execute('SELECT * from test_table;')

# Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cursor.fetchall()

# View results
for row in results:
    print(type(row), row)


# Inserts!!!


