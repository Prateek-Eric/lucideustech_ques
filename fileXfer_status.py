#!/usr/bin/python

##########################################
#
#    Description : File transfer Status
#    How to Run  : python fileXfer_status.py (file_name)
#    Author : Prateek Sharma
#    OS : Redhat 6.0 x86_64
#    Python ver : 2.6.6
#
##########################################

import os
import sys
import subprocess

file_name = str(sys.argv[1])

ret_value = subprocess.Popen(["fuser",file_name],stdout=subprocess.PIPE).communicate()[0]

if ret_value.strip().split('\n')[0]:
	print  file_name +" is being transfered"
else:
	print file_name +" is not being transfered"

