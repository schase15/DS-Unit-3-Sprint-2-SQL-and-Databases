# Import pandas
import pandas as pd

# Read in CSV
df = pd.read_csv('buddymove_holidayiq.csv')

# Make sure it was done properly
df.shape

# Open a connection to the blank buddymove sqlite file
# Imports
import sqlite3
import os

# Set Datapath
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")

# Set up connection and cursor
connection = sqlite3.connect(DATABASE_FILEPATH)

# Save to SQL
df.to_sql('review', con=connection, index= False, if_exists='replace')
