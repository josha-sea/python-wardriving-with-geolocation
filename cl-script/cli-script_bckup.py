'''

CLI-Script to track nearby wifi APs and store in sqlite database

'''

# Imports
import subprocess
import sys

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

	print(f"[ We found {len(results)} wifis! ]")
	print("\n")
	for res in results:
		print(f"Signal: {res.signal} - BSSID: {res.bssid} - SSID: {res.ssid}")

	pause()
	exit_()

def scan_with_save():
	clear_screen()
	print("[---------------------------------]")
	print("[<---> SCANNING WITH SAVING <---->]")
	print("[---------------------------------]")
	print("[-----[ PRESS CTRL-C TO STOP ]----]")
	print("\n")

	connection = database.connect()
	database.create_table(connection)

	interface = scanner.get_interface()

	while True:
		try:

			results = scanner.scan(interface)
			if results:
				print(f"[+] We found {len(results)} results!")
				for res in results:
					database.add_wifi(connection, res.bssid, res.ssid)
			else:
				print("[-] No wifis found!")
			


		except KeyboardInterrupt:
			print("Scanning was interrupted!")
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

	connection = database.connect()
	results = database.get_all_wifis(connection)
	#print(results)
	for res in results:
		print(f"ID {res[0]}: BSSID: {res[1]} SSID: {res[2]}")

	connection.close()
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




menu()

