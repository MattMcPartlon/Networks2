#!/usr/bin/python
import os

for y in range(0,193, 1):
	print(str(y))    
	os.system("ns script" + str(y) + ".tcl")

