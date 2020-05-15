# Module 4 assignment
# Use the titanic PostgreSQL that we have already created to answer some queries


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

# Create cursor
cursor = connection.cursor()

# Queries: 

# How many passengers survived?
query = "Select count(Distinct id) From passengers Where survived=1"

# Execute query - In Postgresql we have to do the execute and fetch in two different steps
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print results - 342
print('-----------')
print('Number of passengers who survived')
print(results[0])

# How many passengers died?
query = "Select count(Distinct id) From passengers Where survived=0"

# Execute query - In Postgresql we have to do the execute and fetch in two different steps
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print results - 545
print('-----------')
print('Number of passengers who died')
print(results[0])

# How many passengers in each class?
query = "Select pclass, count(Distinct id) From passengers Group By pclass"

# Execute query - In Postgresql we have to do the execute and fetch in two different steps
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print results
print('-----------')
print('Number of passengers in each class')
for row in results:
    print(row)

# How many passengers survived/died within each class?

query= '''
SELECT
	CASE
	WHEN pclass = 1 and survived = 1 Then 'first_class_survived'
	WHEN pclass = 1 and survived = 0 Then 'first_class_died'
	WHEN pclass = 2 and survived = 1 Then 'second_class_survived'
	WHEN pclass = 2 and survived = 0 Then 'second_class_died'
	WHEN pclass = 3 and survived = 1 Then 'third_class_survived'
	WHEN pclass = 3 and survived = 0 Then 'third_class_died'
	Else 'todo'
	end as class_mortality,
	count(distinct id) as mortality_count
From passengers
Group by class_mortality
'''

# Execute query - In Postgresql we have to do the execute and fetch in two different steps
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print results
print('-----------')
print('Number of passengers who survived/died in each class')
for row in results:
    print(row)

# Average age of survived vs died
query = "Select survived, avg(age) as avg_age From passengers Group By survived"

# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average age survived: ', results[0][1])
print('Average age died: ', results[1][1])

# Average age of each pclass
query = "Select pclass, avg(age) as avg_age From passengers Group By pclass"

# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average age first class: ', results[0][1])
print('Average age second class: ', results[1][1])
print('Average age third class: ', results[2][1])

# Average fare by pclass

query = '''
Select 
	pclass,
	avg(fare) as avg_fare
From passengers
Group By pclass
'''
# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average fare first class: ', results[0][1])
print('Average fare second class: ', results[1][1])
print('Average fare third class: ', results[2][1])


# Average fare by survived
query = '''
Select 
	survived,
	avg(fare) as avg_fare
From passengers
Group By survived
'''
# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average fare survived: ', results[0][1])
print('Average fare died: ', results[1][1])


# Average number of siblings/spouses on average by class
query = '''
Select 
	pclass,
	avg(sib_spouse_count) as avg_sib_spouse
From passengers
Group By pclass
'''
# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average Sibling/Spouse in First class: ', results[0][1])
print('Average Sibling/Spouse in Second class: ', results[1][1])
print('Average Sibling/Spouse in Third class: ', results[2][1])


# Average number of siblings/spouses on average by survival
query = '''
Select 
	survived,
	avg(sib_spouse_count) as avg_sib_spouse
From passengers
Group By survived
'''
# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average Sibling/Spouse in survivors: ', results[0][1])
print('Average Sibling/Spouse in non-survivors: ', results[1][1])


# Average number of siblings/spouses on average by class
query = '''
Select 
	pclass,
	avg(parent_child_count) as avg_parent_child
From passengers
Group By pclass
'''
# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average Parent/Child in First class: ', results[0][1])
print('Average Parent/Child in Second class: ', results[1][1])
print('Average Parent/Child in Third class: ', results[2][1])


# Average number of parent_child on average by survival
query = '''
Select 
	survived,
	avg(parent_child_count) as avg_parent_child
From passengers
Group By survived
'''
# Execture query
cursor.execute(query)

# Get results
results = cursor.fetchall()

# Print
print("--------")
print('Average Parent/Child in survivors: ', results[0][1])
print('Average Parent/Child in non-survivors: ', results[1][1])



