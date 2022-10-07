'''
Main Script - CLI-Tool
'''
import database
import gps
import scanner

import os
from datetime import datetime
import logging

DATABASE_DIR = "./database"
DATABASE_PATH = f"{DATABASE_DIR}/data.db"
LOGS_DIR = "./logs"
LOG_PATH = f"{LOGS_DIR}/{__name__}.log"

def check_dirs():
	if not os.path.exists(DATABASE_DIR):
		os.mkdir(DATABASE_DIR)
	if not os.path.exists(LOGS_DIR):
		os.mkdir(LOGS_DIR)

def greetings():
	print("Wifi Mapper by Josha Sea")
	print("...")
	print("Start scanning and location mapping...")
	print("Results are stored in database-directory (./database/)...")
	print("Make sure gps-adapter is plugged in!")
	print("Make sure wifi is turned off!")
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
					print(f"We found {len(results)} wifis at location {location}")

					for res in results:
						database.add_wifi(connection, res.bssid, res.ssid, res.freq)

					for res in results:
						date_time = datetime.now()
						database.add_signal(connection, res.bssid, res.signal, location["latitude"], location["longitude"] , date_time)
			except:
				logger.exception("Main loop failed")
				exit(-1)
	except KeyboardInterrupt:
		print("")
		print(f"Currently we have {database.get_wifi_count(connection)} entrys in the wifi-database.")
		print("Script interrupted by User")
		exit(0)

if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	logger.setLevel(logging.ERROR)
	logger.propagate = False


	formatter = logging.Formatter("[%(asctime)s:%(name)s:%(levelname)s:%(message)s]")

	file_handler = logging.FileHandler(LOG_PATH)
	file_handler.setFormatter(formatter)

	logger.addHandler(file_handler)

	greetings()
	check_dirs()
	main()