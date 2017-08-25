#!/usr/bin/python

##############################################################
#   	Desciption : check disable status from config file /etc/xinetd.d/telnet
#	Name : Prateek Sharma
#	How to Run : python telnet_status.py
#	OS : RedHat 6.0 x86_64
##############################################################

prop = {}

config_file = '/etc/xinetd.d/telnet'

with open(config_file) as file:	
	for line in file:
		name,var = line.partition("=")[::2]
		prop[name.strip()] = var

if (prop['disable'].strip() == 'no'):
	print "Telnet is Enabled"
else:
	print "Telnet is Disabled"
