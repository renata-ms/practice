#!/usr/bin/env python
# -*-coding: UTF-8 -*-
dic = {'one':'dom', 'two':'doma', 'many':'domov'}
def humanizer(n, dic):
	if type(n) != int:
		print "You enter not a number. Please, enter a number!"
	elif type(dic) != dict:
		print "You enter not a dictionary. Please, enter a dictionary!"
	else:
		if n == 1:
			print str(n) + " " + dic['one']
		elif n > 1 and n < 5:
			print str(n) + " " + dic['two']
		else:
			print str(n) + " " + dic['many']
		
humanizer(1, dic)
humanizer(2, dic)
humanizer(138, dic)			
