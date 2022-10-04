import pywifi
import time

# Main Module Object
wifi = pywifi.PyWiFi()

# Interface object
interface = wifi.interfaces()[0]


print("Scanning ...")

# Scan for wifi access points
interface.scan()

# Sleep for 8 sec. (recommended: 2-8 sec.)
time.sleep(8)

print("Scan-Results:")
# Note: Results are in list-format
results = interface.scan_results()

print("Total results: " + str(len(results)))

# Show all attributes of profile-object with dir()
#print(dir(results[0]))

print("Signal:")
# Note: Signal outputs in dBm-format; from 0 to -100
# Note: -40 is better signal than -80, bc -80 is further away from 0
print(results[0].signal)

exit()

# Print all available wifi access points with bssid and ssid
for i in results:
	bssid = i.bssid
	ssid = i.ssid 
	print(f"{bssid}:{ssid}")
