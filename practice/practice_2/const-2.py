#!/usr/bin/env python
# -*-coding: UTF-8 -*-

dic = {'pi': 3.141592653589793238462, 'e': 2.718281828459045235360,'y': 0.577215664901532860606,'a': 2.502907875095892822283, 'K': 0.76422365358922066}
try:
	c = raw_input("Enter const and number like <name>:<number>\n")
	d = int(c.find(":"))
	w = c[0:d]
	n = c[d+1:]
	print w + " =  " + str(round(float(dic[w]), int(n)))
except:
	print "... wrong const(("

