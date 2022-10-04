import serial 

phone = serial.Serial("com7", 4800, timeout=5)

path = "gpsdata/gpsdata.txt"



try:
	while True:
		ser_bytes = phone.readline()
		decoded_bytes = ser_bytes.decode("utf-8")
		data = decoded_bytes.split(",")
		if data[0] == "$GPRMC":
			print(data)
			if data[2] == "A":
				with open(path, "a") as f:
					f.write(f"UTC: {data[1]}, Latitude: {data[3]}, Logitude: {data[5]}\n")
except KeyboardInterrupt:
	print("Script interrupted... ")