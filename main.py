from tkinter import *
from math import tan, radians
from random import randint
from dronekit import connect

vehicle = connect("tcp:127.0.0.1:5762", wait_ready=True)

root = Tk()
root.geometry("500x500")
canvas = Canvas(root, bg="white", height=500, width=500)
canvas.pack()
line = canvas.create_line(100,20,100,20, fill="red")

y1 = 250
y2 = 250

def update():
	global y1
	global y2
	pm = 0 # plus-minus

	# roll = randint(-20, 20)
	print("first roll: {}".format(vehicle.attitude.roll))
	roll = int(vehicle.attitude.roll*57.3*(-1))


	print("roll angle: {}".format(roll))
	if roll < 0:
		roll *= -1
		pm = tan(radians(roll)) * 100
		y1 = 250 - pm
		y2 = 250 + pm
	elif roll == 0:
		y1 = y2 = 250
	elif roll > 0:
		pm = tan(radians(roll)) * 100
		y1 = 250 + pm
		y2 = 250 - pm

	print("y1: {}, y2: {}".format(y1, y2))
	canvas.coords(line, 150, y1, 350, y2)
	root.after(50, update)

update()
root.mainloop()