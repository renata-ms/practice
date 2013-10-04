#!/usr/bin/env python
# -*-coding: UTF-8 -*-
dic = {'january': 01, 'february':02,'march':03,'april':04, 'may':05, 'june':06}
dic['july'] = 07
dic['october'] = 10
dic['november'] = 11
dic['december'] = 12
dic['august'] = 8
dic['september'] = 9
try:
	month = raw_input("Please, enter any month\n")
	print "You enter " + month + "! And it's a..."
	print "... " + str(dic[month]) + " month in the year!"
except:
	print "... wrong month(("

