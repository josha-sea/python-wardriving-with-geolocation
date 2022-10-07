'''
Main Script - CLI-Tool
'''
import database
import gps
import scanner

import os
from datetime import datetime

DATABASE_DIR = "./database"
DATABASE_PATH = f"{DATABASE_DIR}/data.db"

def check_database_dir():
	if not os.path.exists(DATABASE_DIR):
		os.mkdir(DATABASE_DIR)

def greetings():
	print("Wifi Mapper by Josha Sea")
	print("...")
	print("Start scanning and location mapping...")
	print("Results are stored in database-directory (./database/)...")
	print("GPS Module must be on serial-port 'COM7'")
	print("Make sure wifi is turned off")
	print("Good luck!")
	print()

def main():
	connection = database.connect(DATABASE_PATH)
	database.create_tables(connection)
	interface = scanner.get_interface()
	com_port = input("Please type the port number of the COM-Connection: ")
	gps_module = gps.get_gps(com_port)

	try:
		while True:
			try:
				results = scanner.scan(interface)
				location = gps.get_location(gps_module)
				

				if results:
					print(f"We found {len(results)} at location {location}")

					for res in results:
						database.add_wifi(connection, res.bssid, res.ssid, res.freq)

					for res in results:
						date_time = datetime.now()
						database.add_signal(connection, res.bssid, res.signal, location["latitude"], location["longitude"] , date_time)
			except Exception as e:
				raise e
	except Exception as e:
		raise e
	except KeyboardInterrupt:
		print("")
		print(f"Currently we have {database.get_wifi_count(connection)} entrys in the wifi-database.")
		print("Script interrupted by User")
		exit(0)

if __name__ == '__main__':
	greetings()
	check_database_dir()
	main()