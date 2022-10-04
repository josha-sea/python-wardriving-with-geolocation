'''
SQLite3 Module Script
'''

# Import module
# Note: sqlite3 is in the python standard module index
import sqlite3 

# Establish connection and
# create database-file if not already exists
con = sqlite3.connect("data.db")

# Create cursor object to execute sqlite commands
cur = con.cursor()

# Execute commands using cursor object
# -> cur.execute()

# Create table
cur.execute(''' CREATE TABLE books(name text, price )''')