'''
GPS Script with GPS-Module 
'''

import serial
import pynmea2
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

def get_gps(com_port):
	try:
		return serial.Serial(f"com{com_port}", 4800)
	except:
		print(f"Something went wrong. Take a look at {__name__}.log.")
		logger.exception("Failed to get serial COM-connection")
		sys.exit(-1)

def get_location(gps):
	fail_counter = 0
	try:
		while True:
			try:
				ser_bytes = gps.readline()
				decoded_bytes = ser_bytes.decode("utf-8")
				nmea = pynmea2.parse(decoded_bytes, check=False)
				if nmea.sentence_type == "RMC" and nmea.is_valid:
					return {
						"latitude": str(nmea.latitude),
						"longitude": str(nmea.longitude)
					}
					break
				else:
					fail_counter += 1
					if fail_counter > 10:
						return {
						"latitude": "NO GPS",
						"longitude": "NO GPS"
						}
						break
			
			except:
				print(f"Something went wrong. Take a look at {__name__}.log.")
				logger.exception("Failed to read and return gps-data")
				sys.exit(-1)

	except KeyboardInterrupt:
			print()
			print(f"Script interruppted by User @ {__name__} module")
			return "break"