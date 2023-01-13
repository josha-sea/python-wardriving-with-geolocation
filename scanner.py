'''
Wifi-Scanner Script
'''

from time import sleep
import pywifi
import logging
import sys


LOG_PATH = f"../logs/{__name__}.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.propagate = False
formatter = logging.Formatter("[%(asctime)s:%(name)s:%(levelname)s:%(funcName)s:%(message)s]")
file_handler = logging.FileHandler(LOG_PATH)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def get_interface():
	try:
		wifi = pywifi.PyWiFi()
		return wifi.interfaces()[0]
	except:
		print(f"Something went wrong. Take a look at {__name__}.log.")
		logger.exception("Failed to get wifi-interface")
		sys.exit(-1)

def scan(interface):
	try:
		interface.scan()
		sleep(5)
		return interface.scan_results()
	except KeyboardInterrupt:
		print()
		print(f"Script interruppted by User @ {__name__} module")
		return "break"
	except:
		print(f"Something went wrong. Take a look at {__name__}.log.")
		logger.exception("Failed to scan for wifis")
		sys.exit(-1)