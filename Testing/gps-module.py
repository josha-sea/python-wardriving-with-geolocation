import serial 

try:
	gps = serial.Serial("com7", 4800)
except Exception as e:
	print(e)
try:
	while True:
		ser_bytes = gps.readline()
		decoded_bytes = ser_bytes.decode("utf-8")
		data = decoded_bytes.split(",")
		if data[0] == "$GPRMC":
			print(data)
except Exception as e:
	print(e)
except KeyboardInterrupt:
	print("Interrupted by user")	
