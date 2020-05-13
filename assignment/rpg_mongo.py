# Module 3 assignment
# Insert RPG data into MongoDG instance

# Imports
import pymongo
import os
from dotenv import load_dotenv
import pandas
import sqlite3

# Load credentials from .env file
load_dotenv()

# Retrieve credentials in .env file
DB_USER = os.getenv("MONGO_RPG_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_RPG_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_RPG_CLUSTER_NAME", default="OOPS")

# Create connection
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

# Set Mongo client
client = pymongo.MongoClient(connection_uri)

# Use client to create a specific database
# Database won't exist until we insert data
db = client.rpg_db

# Create a collection (similar to a table) inisde the new database
# Also will not exist until data is inserted
collection = db.rpg_collection

# Insert data into the collection object
# Use the data from one of the tables in the rpg_db.sqlite3

# Retrieve data from rpg_db.sqlite3
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

# Convert the DF to a dictionary to insert into Mongo
records = armory_items.to_dict("records")

# Insert dictionary into Mongo
collection.insert_many(records)

# Check to make sure they were inserted
# Count the number of documents (rows) - should be 174
print('DOCS:', collection.count_documents({}))

#### WRITTEN QUESTIONS ####

'''
I found working with MongoDB to be very similar to working with PostgreSQL. Things might be
named differently and queries are asked in different ways but a lot of the concepts are the same.
I like that PostgreSQL is a little more rigid and structured. It helps prevent errors from not
being careful when inputing values. It is also easier to create queries because you are using intuitive
words like Select, where, is in etc... However, I found MongoDB a little easier when writing in python.
The syntax of the queries makes more sense than writting out a string. I also felt more comfortable
manipulating the results of a query because it was stored in a list instead of an object.
'''