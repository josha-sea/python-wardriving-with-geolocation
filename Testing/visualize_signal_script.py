'''

Script with tkinter and pywifi
to visualize signal strengh of surounding wifi access points
by drawing cirles with signal strenght as radius

'''

# Imports
import pywifi
from tkinter import *
import time  

# Pywifi: Scan for Wifi APs

wifi = pywifi.PyWiFi()

interface = wifi.interfaces()[0]

interface.scan()

time.sleep(8)

results = interface.scan_results()


# Tkinter

def create_circle(x, y, r, canvas_name):

	x0 = x - r  
	y0 = y - r
	x1 = x + r
	y1 = y + r
	return canvas_name.create_oval(x0, y0, x1, y1)


root = Tk()
canvas = Canvas(root, bg="gray", height=600, width=600)

# Loop wifi APs and create circles
# Note: Multiply with 2 is option;
for r in results:
	create_circle(600/2, 600/2, abs(r.signal)*2, canvas)


canvas.pack()
root.mainloop()