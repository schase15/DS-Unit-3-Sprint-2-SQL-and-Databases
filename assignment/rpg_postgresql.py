# Part 1 of module 2 assignment

# Set up and load rpg data into PostgreSQL
# rpg data is store in rpg_db.sqlite3

# Imports
import sqlite3
import pandas
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json

## Retrieve specific table from rpg_db.sqlite3
# Point to file
database_filepath = os.path.join(os.path.dirname(__file__), "..", 'data', "rpg_db.sqlite3")

# Establish connection to sqlite3 database in files
lite_con = sqlite3.connect(database_filepath)

# Establish cursor to perform queries
lite_cursor = lite_con.cursor()

# Query to pull out table
get_table = '''
select *
from armory_item
'''

# Set table to variable name 
armory_items = pandas.read_sql(sql = get_table, con = lite_con)

# NOW YOU HAVE THE DATA STORED AS A DF

## Create instance of PostgreSQL on ElephantSQL
# Save credentials in .env file

# Load contents of .env file which holds credentials.
load_dotenv()

# Use environment variables to load credentials, so other peopole can access the files and not see the credentials
db_name = os.getenv('DB_name', default= 'OOPS')
db_user = os.getenv('DB_user', default= 'OOPS')
db_pwd = os.getenv('DB_pwd', default= 'OOPS')
db_host = os.getenv('DB_host', default= 'OOPS')

## Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=db_name, user=db_user,
                        password=db_pwd, host=db_host)
print(type(connection))


# Create cursor to perform queries
cursor = connection.cursor()
print(type(cursor))

# CREATE TABLE - set up
# name table, add column names and types of data they hold
table_creation_query = """
CREATE TABLE IF NOT EXISTS armory_items (
  item_id SERIAL PRIMARY KEY,
  name varchar(200),
  value INTEGER,
  weight INTEGER
)
"""

# Execute create table
cursor.execute(table_creation_query)

## Insert data from rpg db to table we just created
insertion_query = f"INSERT INTO armory_items (item_id, name, value, weight) VALUES %s"

# Turn df into dictionary
records = armory_items.to_dict("records")


# Turn dictionary into list of tuples
# Iterate through rows, grabbing one item from each key name (old column headers) in dictionary
list_of_tuples = [(r['item_id'], r['name'], r['value'], r['weight']) for r in records]


# Same way to create a list of tuples, only one step
# list_of_tuples = list(armory_items.to_records(index= False))


# Use execute values to insert data into table
execute_values(cursor, insertion_query, list_of_tuples)

# Save the transaction - commit changes to PostgreSQL site
connection.commit()
cursor.close()
connection.close()
