#!/usr/bin/env python
# -*-coding: UTF-8 -*-
import calendar
try:
	year = raw_input("Please, enter any year\n")
	print "You enter " + str(year) + "! And it's a..."
	year = int(year)
	if calendar.isleap(year):
		print "...LEAP YEAR!!!"
	else:
		print "...not leap year =("
except ValueError:
	print "... not a number. Please, try again later."

