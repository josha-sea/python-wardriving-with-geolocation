'''
Main Script - CLI-Tool
'''


import os
from datetime import datetime
import logging

DATABASE_DIR = "../database"
DATABASE_PATH = f"{DATABASE_DIR}/data.db"
LOGS_DIR = "../logs"
LOG_PATH = f"{LOGS_DIR}/{__name__}.log"

def check_dirs():
	if not os.path.exists(DATABASE_DIR):
		os.mkdir(DATABASE_DIR)
	if not os.path.exists(LOGS_DIR):
		os.mkdir(LOGS_DIR)

def greetings():
	print("[#] Wifi Mapper by Josha Sea")
	print("...")
	print("[~] Start scanning and location mapping...")
	print(f"[+] Results are stored in database-directory ({os.path.abspath(DATABASE_DIR)})")
	print(f"[+] Logs are stored in logs-directory ({os.path.abspath(LOGS_DIR)})")
	print("[!] Make sure gps-adapter is plugged in")
	print("[!] Make sure wifi is turned off")
	print("[#] Good luck!")
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

				if results == "break" or location == "break": break

				if results:
					print(f"We found {len(results)} wifis at location {location}")

					for res in results:
						database.add_wifi(connection, res.bssid, res.ssid, res.freq)

					for res in results:
						date_time = datetime.now()
						database.add_signal(connection, res.bssid, res.signal, location["latitude"], location["longitude"] , date_time)
				else:
					continue
			except:
				logger.exception("Main loop failed")
				break
	except:
		print()
		print(f"Something went wrong. Take a look at {__name__}.log.")
		logger.exception(f"Somethink went wrong @ {__name__} module")
	finally:
		print()
		print(f"Currently we have {database.get_wifi_count(connection)} entrys in the wifi-database.")


if __name__ == '__main__':
	check_dirs()
	import database
	import gps
	import scanner

	logger = logging.getLogger(__name__)
	logger.setLevel(logging.ERROR)
	logger.propagate = False
	formatter = logging.Formatter("[%(asctime)s:%(name)s:%(levelname)s:%(funcName)s:%(message)s]")
	file_handler = logging.FileHandler(LOG_PATH)
	file_handler.setFormatter(formatter)

	logger.addHandler(file_handler)

	
	greetings()
	
	main()