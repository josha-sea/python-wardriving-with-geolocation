'''

Tkinter-Script to draw cicrcle

'''

# Imports module
from tkinter import *

# Vars
height = 500 
width = 500

center = [height/2, width/2]

# Functions
# Helper function to draw circle

def create_circle(x, y, r, canvas_name):

	x0 = x - r  
	y0 = y - r
	x1 = x + r
	y1 = y + r
	return canvas_name.create_oval(x0, y0, x1, y1)


# Main script
root = Tk()

canvas = Canvas(root, bg="gray", height=height, width=width)
canvas.pack()

create_circle(center[0], center[1], 50, canvas)

root.mainloop()