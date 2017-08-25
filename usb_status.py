#! /usr/bin/python

#######################################################################
#	Description : /etc/modprobe.d/blacklist.conf contains usb-storage or not
#	Name : Prateek Sharma
#	How to run : Python usb_status.py
#	OS : RedHat 6.0 x86_64
########################################################################

import os
import subprocess

cmd = "cat /etc/modprobe.d/blacklist.conf | grep -i 'usb-storage'"

output = subprocess.Popen( cmd, stdout=subprocess.PIPE,shell=True)

(usb_stat,err) = output.communicate()

usb_nam_list = (usb_stat.rstrip()).split('\n')

if not usb_nam_list[0]:
	print "USB Enabled"
else:
	print "USB Disabled"
