#!/usr/bin/python3
import subprocess
import cgi

print('content-type: text/html')
print()
data = cgi.FieldStorage()
cmdd = data.getvalue("cmd")
cmd = "sudo {}".format(cmdd)
output = subprocess.getoutput(cmd)
