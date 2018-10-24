#coding=utf-8
#!/usr/bin/env python

import os

def getkey(str):
    if '=' not in str:
        print u'Error'
    else:
        L = str.split('=')
        #print L
        key = L[1].split()
        #print key
    return key

def getname(keyword):
    with open(u'D:\python_project\login_check\passwd.txt' , 'r') as file:
        L , M = file.readlines() , []
        for line in L:
            if keyword in line and 'name' in line:
                #print line
                username = getkey(line)
                M.append(username)
                #print u'用户名是 %s' % (username)
            if keyword in line and 'password' in line:
                #print line
                password = getkey(line)
                M.append(password)
                #print u'密码 %s' % (password)
    return M

#getname('ZDM')

'''
username , password = getname('ZDM')
print username , password
'''