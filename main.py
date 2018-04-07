print "Welcome to Russian Roulette."
import sys
x = 0
y = 0

import random
min = 1
max = 8


for y in range (0,8):
	x = random.randint(1, 8)
	print str(x)
	y = y + 1
	if x == 8:
		print "You died; " + "you lasted " + str(y) + " turn(s)."
		sys.exit(0)
	if y == 8:
		print "You won."
		sys.exit(0)