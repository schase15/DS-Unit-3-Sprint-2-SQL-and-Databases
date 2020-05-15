# Import pandas
import pandas
import os
import sqlite3

# Read in CSV
# df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv')

# Better way to read in dataframe
CSV_path = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "buddymove_holidayiq.csv")
df = pandas.read_csv(CSV_path)
# to start index at 1 (resembling primary key behavior)
df.index += 1

# You now have the CSV saved as a dataframe
# Make sure it was done properly
df.shape


# Create a blank sqlite3 page to move data to
# Open a connection to the blank buddymove sqlite file

# Set Datapath
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")

# Set up connection and cursor
connection = sqlite3.connect(DATABASE_FILEPATH)

# Save to SQL
df.to_sql('review', con=connection, index= False, if_exists='replace')
