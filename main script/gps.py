'''
GPS Script with GPS-Module 
'''

import serial
import pynmea2

def get_gps():
	try:
		return serial.Serial("com7", 4800)
	except:
		print("No GPS module found")
		return False

def get_location(gps):
	fail_counter = 0
	while True:
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