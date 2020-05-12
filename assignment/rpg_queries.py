# Assignment part 1

# Imports
import sqlite3
import os


# Set Datapath
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

# Set up connection and cursor
connection = sqlite3.connect(DATABASE_FILEPATH)

# Use row factory so that we can call columns by name instead of index
connection.row_factory = sqlite3.Row
print(type(connection))
cursor = connection.cursor()
print(type(cursor))


# Query - How many total Characters are there?
query = "Select count(Distinct character_id) as character_count From charactercreator_character"

# Results - 302
result = cursor.execute(query).fetchall() #> LIST

# Print results
for row in result:
    print("---------")
    print('Total number of characters')
    print(row["character_count"])


# Query - How many of each specific subclass?
# Cleric
query = "Select count(Distinct character_ptr_id) as character_count From charactercreator_cleric"

# Results - 75
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of Cleric characters')
    print(row["character_count"])

# Fighter
query = "Select count(Distinct character_ptr_id) as character_count From charactercreator_fighter"

# Results - 68
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of Fighter characters')
    print(row["character_count"])

# Mage
query = "Select count(Distinct character_ptr_id) as character_count From charactercreator_mage"

# Results - 108
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of Mage characters')
    print(row["character_count"])

# Necromancer 
query = "Select count(Distinct mage_ptr_id) as character_count From charactercreator_necromancer"

# Results - 11
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of Necromancer characters')
    print(row["character_count"])

# Thief
query = "Select count(Distinct character_ptr_id) as character_count From charactercreator_thief"

# Results - 51
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of Thief characters')
    print(row["character_count"])

# How many total items?
query = "Select count(Distinct item_id) as item_count From armory_item"

# Results - 174
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of items')
    print(row["item_count"])

# How many of the Items are weapons?
query = "Select count(Distinct item_ptr_id) as weapon_count From armory_weapon"

# Results - 37
result = cursor.execute(query).fetchall()

# Print results
for row in result:
    print("---------")
    print('Total number of items that are weapons')
    print(row["weapon_count"])

# How many are not weapons - 137
print("---------")
print('Total number of items that are not weapons')
print(174 - 37)

# How many Items does each character have? (Return first 20 rows)
query = "Select character_id, count(item_id) as item_count From charactercreator_character_inventory Group By character_id Limit 20"

# Results
result = cursor.execute(query).fetchall()

# Print results
print("---------")
print('Item counts for first 20 characters')
for row in result:
    print(row["character_id"], row["item_count"])

# How many weapons does each character have? (Return first 20)
# Left join character inventory with armory weapon to keep all of the character id's even if they don't have a weapon
# Group by character ID and count weapon id

query = "SELECT character_id, count(item_ptr_id) as weapon_count FROM charactercreator_character_inventory LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id GROUP BY character_id LIMIT 20 "

# Results
result = cursor.execute(query).fetchall()

# Print results
print("---------")
print('Weapon counts for first 20 characters')
for row in result:
    print(row["character_id"], row["weapon_count"])

# On average, how many items and weapons does each character have
# Use the joined table from above, keep item_id as well
# Use as a subquery and return the average of weapon count and item count

query = 'SELECT AVG(weapon_count) as avg_weapon, AVG(item_count) as avg_item FROM (SELECT character_id, count(item_ptr_id) as weapon_count, count(item_id) as item_count FROM charactercreator_character_inventory LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id GROUP BY character_id)'

# Results
result = cursor.execute(query).fetchall()

# Print results
print("---------")
print('Average item count')
for row in result:
    print(row["avg_item"])
print("---------")
print('Average weapon count')
for row in result:
    print(row["avg_weapon"])

