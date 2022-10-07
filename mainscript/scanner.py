'''
Wifi-Scanner Script
'''
from time import sleep
import pywifi

def get_interface():
	wifi = pywifi.PyWiFi()
	return wifi.interfaces()[0]

def scan(interface):
	interface.scan()
	sleep(5)
	return interface.scan_results()