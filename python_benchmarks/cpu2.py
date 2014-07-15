#!/usr/bin/env python
import sys
i = 0
while True:
	string=raw_input()
	temp = ''
	for char in string:
		temp += char
	i += 1
	if i == 10000: i = 0
	if i == 0:
		print string 
		sys.stdout.flush()
	else:
		print 
		sys.stdout.flush()
