'''
Database (sqlite3) Script
'''

import sqlite3

# Querys

CREATE_WIFI_TABLE = "CREATE TABLE IF NOT EXISTS wifi (id INTEGER PRIMARY KEY, bssid TEXT UNIQUE NOT NULL, ssid TEXT, frequency INTEGER)"

CREATE_SIGNALS_TABLE = "CREATE TABLE IF NOT EXISTS signals (id INTEGER PRIMARY KEY, signal_strenght INTEGER, latitude TEXT, longitude TEXT,  date_time TEXT, wifi_id INTEGER, FOREIGN KEY (wifi_id) REFERENCES wifi (id))"

INSERT_WIFI = "INSERT INTO wifi (bssid, ssid, frequency) VALUES (?,?,?) ON CONFLICT (bssid) DO NOTHING"

INSERT_SIGNAL = "INSERT INTO signals (signal_strenght, latitude, longitude, date_time, wifi_id) VALUES (?,?,?,?,?)"

FETCH_WIFI_ID = "SELECT id FROM wifi WHERE bssid = (?)"

GET_ALL_WIFIS = "SELECT * FROM wifi"

# Functions
def connect(path):
	return sqlite3.connect(path)

def create_tables(connection):
	with connection:
		connection.execute(CREATE_WIFI_TABLE)
		connection.execute(CREATE_SIGNALS_TABLE)

def add_wifi(connection, bssid, ssid, frequency):
	with connection:
		connection.execute(INSERT_WIFI, (bssid, ssid, frequency))

def add_signal(connection, bssid, signal_strenght, latitude, longitude, date_time):
	with connection:
		wifi_id = connection.execute(FETCH_WIFI_ID, (bssid,)).fetchone()[0]
		connection.execute(INSERT_SIGNAL, (signal_strenght, latitude, longitude, date_time, wifi_id))

def get_wifi_count(connection):
	with connection:
		try:
			return len(connection.execute(GET_ALL_WIFIS).fetchall())
		except:
			print("No wifis in database")
