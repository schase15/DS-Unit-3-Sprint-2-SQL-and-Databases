# inclass/mongo_queries.py

# Imports
import pymongo
import os
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

# # Connection string - from MongoDb website
# mongodb+srv://schase15:<password>@cluster0-mkqyt.mongodb.net/test?retryWrites=true&w=majority

# Broke connection string down into variables so that we can store the credentials in .env file 
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

# Use Mongo client - similar to a connection
client = pymongo.MongoClient(connection_uri)

# Use the client to connect to specific database
# Create a new database by calling it directly on the client
# Doesn't get created until we insert data, exists just in memory
# 'ds14_db' or whatever you want to name it
db = client.ds14_db 

# Create a collection (table) inside of this new database
# Still just in memory, haven't inserted any data yet
# "ds14_collection" or whatever you want to call it
collection = db.ds14_collection 

# Insert data into our collection object - inserting one document at a time
# After inserting data the collection and document will be made
# We can have nested data inside documents, (last two lines as examples)
collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    'fav_icecream_flavors': ['vanilla_bean', 'choc'],
    'stats': {'a':1, 'b':2, 'c': [1,2,3]}
})

# Look at the results
# Count the number of documents (similar to rows)
print("DOCS:", collection.count_documents({})) # SELECT count(distinct.id) from pokemon

# SELECT count(distinct.id) from pokemon WHERE name = 'Pickachu'
print(collection.count_documents({"name": "Pikachu"})) # WHERE clause


# INSERTS
# pass in multiple documents at the same time 

# Create data to insert
mewtwo = {
    "name": "Mewtwo",
    "level": 100,
    "exp": 76000000000,
    "hp": 450,
    "strength": 550,
    "intelligence": 450,
    "dexterity": 300,
    "wisdom": 575
}

blastoise = {
    "name": "Blastoise",
    "lvl": 70,
}

skarmory = {
    "name": "Skarmory",
    "level": 22,
    "exp": 42000,
    "hp": 85,
    "strength": 750,
    "intelligence": 8,
    "dexterity": 57
}

cubone = {
    "name": "Cubone",
    "level": 20,
    "exp": 35000,
    "hp": 80,
    "strength": 600,
    "intelligence": 60,
    "dexterity": 200,
    "wisdom": 200
}


scyther = {
    "name": "Scyther",
    "level": 99,
    "exp": 7000,
    "hp": 40,
    "strength": 50,
    "intelligence": 40,
    "dexterity": 30,
    "wisdom": 57
}

# Insert data
pokemon_team = [mewtwo, blastoise, skarmory, cubone, scyther]

collection.insert_many(pokemon_team)

# Query: count number of documents
# Similar to [SELECT count(distinct.id) from pokemon] when we were doing postgresql
print('DOCS:', collection.count_documents({}))


# Query our database
# SELECT * FROM pokemon WHERE name = 'Pikachu'
pikas = list(collection.find({"name": "Pikachu"})) 

# Now we have a subset of the data where name is equal to Pikachu
# Explore the data
print(len(pikas), "PIKAS")

# Collections automatically assigns primary ids, under key '_id'
print(pikas[0]['_id'])
print(pikas[0]['name'])

# More complex query
# Use collection.find and query operators
# Save queries in list form to variables, saves the results of your query in a list which you can then manipulate
# Get pokemon whose level is 60 or above
# Blastoise is saved as 'lvl' instead of 'level', will not be returned. Need to make sure data is clean
strong = list(collection.find({'level': {'$gte': 60}}))
print(strong)

# Documentation for query operators
# https://docs.mongodb.com/manual/reference/operator/query/

