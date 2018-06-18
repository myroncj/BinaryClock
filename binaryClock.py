import itertools
import time

def move_cursor(x,y):
    print ("\x1b[{};{}H".format(y+1,x+1))

def clear():
    print ("\x1b[2J")

clear()

while 1:
	for z in map(''.join, itertools.product('01', repeat=6)):
	    	for y in map(''.join, itertools.product('01', repeat=6)):
	    			for x in map(''.join, itertools.product('01', repeat=6)):
	    				move_cursor(0,0)
	    				print(z + "\n" + y + "\n" + x)
	    				time.sleep(1)