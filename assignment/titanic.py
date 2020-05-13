# Part 2 of module 2 assignment

# Create an instance of a hosted PostgreSQL on ElephantSQL
# Put credentials to log into PostgreSQL in .env file

# Imports
import os
import pandas
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import numpy as np

# Loads contents of the .env file into the script's environment
load_dotenv()

# Use environment variables to load credentials
DB_NAME = os.getenv('DB_NAME', default= 'OOPS')
DB_USER = os.getenv('DB_USER', default= 'OOPS')
DB_PASSWORD = os.getenv('DB_PASSWORD', default= 'OOPS')
DB_HOST = os.getenv('DB_HOST', default= 'OOPS')

# Connect to hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection))

# Create cursor
cursor = connection.cursor()
print(type(cursor))


## CREATE TABLE - set up

# Pass in the name of the table
# Pass in the column headers and the types of data they need to be

table_creation_query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived INTEGER,
  pclass INTEGER,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age FLOAT,
  sib_spouse_count INTEGER,
  parent_child_count INTEGER,
  fare FLOAT
);
"""

# Create table
cursor.execute(table_creation_query)


## INSERT DATA IN THE TABLE

# Read CSV and save as df
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")
df = pandas.read_csv(CSV_FILEPATH)
df.index += 1 # to start index at 1 (resembling primary key behavior)
print(df.head())

# to get over errors about not being able to work with the numpy integer datatypes
# could alternatively change the datatypes of our dataframe,
# ... or do transformations on our list of tuples later (after reading from the dataframe, before inserting into the table)
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


# Convert dataframe to tuples
list_of_tuples = list(df.to_records(index=True))

breakpoint()

# Create insertion query and execute
insertion_query = "INSERT INTO passengers (id, survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples)

# Save the results back to the PostgreSQL
connection.commit()
cursor.close()
connection.close()
