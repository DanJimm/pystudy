#!/usr/bin/env python
#coding = UTF-8

from socket import  *

HOST = 'localhost'
PORT = 21567
ADDR = (HOST , PORT)
BUFSIZE = 1024

udpCliSock = socket(AF_INET , SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data , ADDR)
    data , ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print  data
udpCliSock.close()