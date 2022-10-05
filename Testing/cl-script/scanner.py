import time
try:
	import pywifi
except:
	print("[ERROR] Can't import pywifi module!")
	print("[ERROR] Activate virtual environtment OR install pywifi module with 'pip install pywifi'")

def get_interface():
	wifi = pywifi.PyWiFi()
	return wifi.interfaces()[0]

def scan(interface):
	interface.scan()
	time.sleep(5)
	return interface.scan_results()
