'''
Wifi-Scanner Script
'''
from time import sleep
import pywifi
import logging


LOG_PATH = f"../logs/{__name__}.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.propagate = False


formatter = logging.Formatter("[%(asctime)s:%(name)s:%(levelname)s:%(message)s]")

file_handler = logging.FileHandler(LOG_PATH)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def get_interface():
	try:
		wifi = pywifi.PyWiFi()
		return wifi.interfaces()[0]
	except:
		logger.exception("Failed to get wifi-interface")
		exit(-1)

def scan(interface):
	try:
		interface.scan()
		sleep(5)
		return interface.scan_results()
	except:
		logger.exception("Failed to scan for wifis")
		exit(-1)