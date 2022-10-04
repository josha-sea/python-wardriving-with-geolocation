'''

CLI-Script to track nearby wifi APs and store in sqlite database

'''

# Imports
import subprocess
import sys
from datetime import datetime
import os

import database
import scanner
import banner

def clear_screen():
	_ = subprocess.call("CLS", shell=True)

def pause():
	print("\n")
	print("[--------[ PRESS ANY KEY TO QUIT ]-------]")
	_ = subprocess.call("PAUSE > NUL", shell=True)


def exit_():
	clear_screen()
	print("THANK YOU!")
	print("Script is closing ...")
	_ = subprocess.call("COLOR 0F", shell=True)
	sys.exit(0)


def scan_without_save():
	clear_screen()
	print("[------------------------------------]")
	print("[<---> SCANNING WITHOUT SAVING <---->]")
	print("[------------------------------------]")
	print("\n")

	interface = scanner.get_interface()
	results = scanner.scan(interface)

	print(f"[*] We found {len(results)} wifis!")
	print("\n")
	for res in results:
		print(f"Signal: {res.signal} Freq: {res.freq}  BSSID: {res.bssid} - SSID: {res.ssid} ")

	pause()
	exit_()

def scan_with_save():

	if not os.path.exists("database"):
		os.mkdir("database")

	clear_screen()
	print("[---------------------------------]")
	print("[<---> SCANNING WITH SAVING <---->]")
	print("[---------------------------------]")
	print("[-----[ PRESS CTRL-C TO STOP ]----]")
	print("\n")

	connection = database.connect()
	database.create_tables(connection)

	interface = scanner.get_interface()

	while True:
		try:

			results = scanner.scan(interface)

			if results:
				print(f"[+] We found {len(results)} results!")
				# Insert wifis
				for res in results:
					database.add_wifi(connection, res.bssid, res.ssid, res.freq)
				# Insert signals
				for res in results:
					date_time = datetime.now().isoformat()
					database.add_signal(connection, res.bssid, res.signal, "Wien", date_time)
			else:
				print("[-] No wifis found!")
			


		except KeyboardInterrupt:
			print("\n")
			print("[*] Scanning was interrupted!")
			break

	connection.close()
	pause()
	exit_()

def show_all():
	clear_screen()
	print("[---------------------------------------]")
	print("[<---> SHOW ALL WIFIS IN DATABASE <---->]")
	print("[---------------------------------------]")
	print("\n")

	if os.path.exists("database/data.db"):
		connection = database.connect()
		results = database.get_all_wifis(connection)
		if results:
			for res in results:
				print(f"ID {res[0]}: BSSID: {res[1]} SSID: {res[2]} FREQ: {res[3]}")
		else:
			print("[-] No wifis in database!")
			print("[*] Try scanning and saving!")
		connection.close()
	else:
		print("[-] No database was found!")
		print("[*] Try scanning and saving!")

	
	pause()
	exit_()
	

def menu():
	clear_screen()
	_ = subprocess.call("COLOR 0A", shell=True)

	banner.banner()
	print("[----------------------------------------]")
	print("[---------------[ Options ]--------------]")
	print("[----------------------------------------]")
	print("[  [1] : Scan without saving to database ]")
	print("[  [2] : Scan and save to database       ]")
	print("[  [3] : Show all wifis in database      ]")
	print("[----------------------------------------]")
	print("[--------[ PRESS ANY KEY TO QUIT ]-------]")
	print("\n")
	option = input("Please select an option: ")
	
	if option == "1":
		scan_without_save()
	elif option == "2":
		scan_with_save()
	elif option == "3":
		show_all()
	else:
		exit_()

if __name__ == "__main__":
	menu()
	
