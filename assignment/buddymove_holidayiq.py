# Assignment Part 2

# Imports
import sqlite3
import os

# Set Datapath
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")

# Set up connection and cursor
connection = sqlite3.connect(DATABASE_FILEPATH)

# Use row factory so that we can call columns by name instead of index
connection.row_factory = sqlite3.Row
print(type(connection))
cursor = connection.cursor()
print(type(cursor))

# Query - How many total rows are there?
query = 'SELECT count(distinct "User Id") as num_rows FROM review'

# Results - 249
result = cursor.execute(query).fetchall() #> LIST

# Print results
for row in result:
    print("---------")
    print('Total number of rows')
    print(row["num_rows"])

# Query - How many users reviewed at least 100 nature and 100 shopping
query = 'Select count(DISTINCT "User Id") as nature_shopping From review WHERE Nature >= 100 AND Shopping >= 100'

# Results - 78
result = cursor.execute(query).fetchall() #> LIST

# Print results
for row in result:
    print("---------")
    print('Number of users who reviewed at least 100 in both nature and shopping category')
    print(row["nature_shopping"])

# Query - What are the average number of reviews for each category?
query = '''
Select
	AVG(Sports) as avg_sports,
	AVG(Religious) as avg_religious,
	AVG(Nature) as avg_nature,
	AVG(Theatre) as avg_theatre,
	AVG(Shopping) as avg_shopping,
	AVG(Picnic) as avg_picnic
From review
'''

# Results 
result = cursor.execute(query).fetchall() #> LIST

# Print results
for row in result:
    print("---------")
    print('Average number of reviews for sports')
    print(row["avg_sports"])
for row in result:
    print("---------")
    print('Average number of reviews for religious')
    print(row["avg_religious"])
for row in result:
    print("---------")
    print('Average number of reviews for nature')
    print(row["avg_nature"])
for row in result:
    print("---------")
    print('Average number of reviews for theatre')
    print(row["avg_theatre"])
for row in result:
    print("---------")
    print('Average number of reviews for shopping')
    print(row["avg_shopping"])
for row in result:
    print("---------")
    print('Average number of reviews for picnic')
    print(row["avg_picnic"])