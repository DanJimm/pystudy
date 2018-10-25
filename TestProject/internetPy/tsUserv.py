#!/usr/bin/env python
#coding = UTF-8

from time import ctime
from socket import  *

HOST = ''
PORT = 21567
ADDR = (HOST , PORT)
BUFSIZE = 1024

udpSerSock = socket(AF_INET , SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'Waiting for data ...'
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[ %s ] %s ' % (ctime() , data) , addr)
    print '...receive from and sendto: ' , addr

udpSerSock.close()
