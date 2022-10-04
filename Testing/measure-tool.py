'''
Measuring Tool in Python

-> Measuring wifi signals in dBm-unit 

by LP
'''



import pywifi
import time

wifi = pywifi.PyWiFi()
interface = wifi.interfaces()[0]

# 5 Min to measure
total = 60 * 5
counter = 0
values = []

sum_ = 0

while True:

	if counter == total:
		break

	#print("Scanning...")
	interface.scan()
	#print("Sleeping...")
	time.sleep(5)
	results = interface.scan_results()

	if results:
		print(results[0].signal)
		values.append(abs(results[0].signal))
	else:
		print("[X] No connection found!")
	
	counter = counter + 5

for i in values:
	sum_ = sum_ + i 

middle = sum_/len(values)

values.sort()

print("Finished...")
print("Middle Value: " + str(middle))
print("Extremes:" + str(values[0]) + " " + str(values[-1]))