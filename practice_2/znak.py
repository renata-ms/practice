#!/usr/bin/env python
# -*-coding: UTF-8 -*-

a0 = [['*','*','*','*','*','*','*','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*','*','*','*','*','*','*','*'],]
 
a1 = [[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ','*','*'],
[' ',' ',' ',' ',' ','*',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],]


a2 = [['*','*','*','*','*','*','*','*'],
[' ',' ',' ',' ',' ',' ','*',' '],
[' ',' ',' ',' ',' ','*',' ',' '],
[' ',' ',' ',' ','*',' ',' ',' '],
[' ',' ',' ','*',' ',' ',' ',' '],
[' ',' ','*',' ',' ',' ',' ',' '],
[' ','*',' ',' ',' ',' ',' ',' '],
['*','*','*','*','*','*','*','*'],]

a3 = [['*','*','*','*','*','*','*','*'],
[' ',' ',' ',' ',' ',' ','*',' '],
[' ',' ',' ',' ',' ','*',' ',' '],
[' ',' ',' ',' ','*',' ',' ',' '],
[' ',' ',' ',' ',' ','*',' ',' '],
[' ',' ',' ',' ',' ',' ','*',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
['*','*','*','*','*','*','*','*'],]

a4 = [[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ','*','*'],
[' ',' ',' ',' ',' ','*',' ','*'],
[' ',' ',' ',' ','*',' ',' ','*'],
[' ',' ',' ','*','*','*','*','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],]

a5 = [['*','*','*','*','*','*','*','*'],
['*',' ',' ',' ',' ',' ',' ',' '],
['*',' ',' ',' ',' ',' ',' ',' '],
['*','*','*','*','*','*','*','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
['*','*','*','*','*','*','*','*'],]

a6 = [['*','*','*','*','*','*','*','*'],
['*',' ',' ',' ',' ',' ',' ',' '],
['*',' ',' ',' ',' ',' ',' ',' '],
['*',' ',' ',' ',' ',' ',' ',' '],
['*','*','*','*','*','*','*','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*','*','*','*','*','*','*','*'],]

a7 = [['*','*','*','*','*','*','*','*'],
[' ',' ',' ',' ',' ',' ','*',' '],
[' ',' ',' ',' ',' ','*',' ',' '],
[' ',' ','*','*','*','*','*',' '],
[' ',' ',' ','*',' ',' ',' ',' '],
[' ',' ','*',' ',' ',' ',' ',' '],
[' ','*',' ',' ',' ',' ',' ',' '],
['*',' ',' ',' ',' ',' ',' ',' '],]

a8 = [['*','*','*','*','*','*','*','*'],
[' ',' ','*',' ',' ',' ','*',' '],
[' ',' ',' ','*',' ','*',' ',' '],
[' ',' ',' ',' ','*',' ',' ',' '],
[' ',' ',' ','*','*',' ',' ',' '],
[' ',' ','*',' ',' ','*',' ',' '],
[' ','*',' ',' ',' ',' ','*',' '],
['*','*','*','*','*','*','*','*'],]

a9 = [['*','*','*','*','*','*','*','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*',' ',' ',' ',' ',' ',' ','*'],
['*','*','*','*','*','*','*','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
[' ',' ',' ',' ',' ',' ',' ','*'],
['*','*','*','*','*','*','*','*'],]

try:
	n = int(raw_input("Please, enter a number from 0 to 9\n"))
	if type(n) == int:
		if n == 0:
			for word in a0:										print word			
		elif n == 1:
			for word in a1:	
				print word
		elif n == 2:
			for word in a2:
				print word
		elif n == 3:
			for word in a3:
				print word
		elif n == 4:
			for word in a4:
				print word
		elif n == 5:
			for word in a5:
				print word
		elif n == 6:
			for word in a6:
				print word
		elif n == 7:
			for word in a7:
				print word
		elif n == 8:
			for word in a8:
				print word
		elif n == 9:
			for word in a9:
				print word
		else:
			print "You enter too big or too small number!" 	
except:
	print "You enter not a number!"
