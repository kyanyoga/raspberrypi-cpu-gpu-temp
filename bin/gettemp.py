#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Written By: Gus Segura - Blueskymetrics.com
   RaspberryPI GPU and CPU temperature function library
"""

from __future__ import division
import subprocess

def getcput():
	# read cpu temperature file
	f = open("/sys/class/thermal/thermal_zone0/temp","r") # open temperature file
	# print(f.read())
	cputemp  =  int(f.read()) / 1000
	# print (cputemp)
	return cputemp

def getgput():
	# read gpu temperature from command
	gputemp = subprocess.check_output(['/opt/vc/bin/vcgencmd','measure_temp']) 
	gputemp = float(gputemp[5:gputemp.index("'")]) * 100
	gputemp = round(gputemp /100, 2)
	# print gputemp
	return gputemp

if __name__ == '__main__':
	print getcput()
	print getgput()
