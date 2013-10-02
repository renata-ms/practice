#!/usr/bin/env python
# -*-coding: UTF-8 -*-
import calendar

year = raw_input("Please, enter any year\n")
print "You enter " + year + "! And it's a..."
year = int(year)
if calendar.isleap(year):
	print "LEAP YEAR!!!"
else:
	print "not leap year =("
