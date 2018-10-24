#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #导入鼠标操作
from selenium.webdriver.common.keys import Keys #导入键值操作
import time
import traceback
import getname

signpage = 'https://www.smzdm.com/' #ZDM签到登录页

#从文件中获取到用户名和密码的序列
a , M = 1 , getname.getname('ZDM')
num = len(M) / 2
print u'一共有%d个用户需要进行签到' % (num)
print u'用户名和密码为:'
print M

while a <= num:
    print u'进行用户%d的签到' % (a)
    #用户名和密码赋值
    myusername = M[(a*2 - 2)]
    mypassword = M[(a*2 - 1)]
    browser = webdriver.Chrome() #初始化浏览器对象
    browser.maximize_window() #浏览器最大
    try:
        browser.get(signpage) #打开登录页面
        browser.implicitly_wait(2)#隐式等待
        #判定是否登录
        name_str = browser.find_element_by_xpath(".//*[@id='index-head']/div[3]/div[1]/div[3]/div[1]").text
        if 'JimDD' in name_str:
            print u'已登录'
        else:
            print u'用户%d没有登录，现在登录' % (a)
            #切换到账户登录
            jumplogin = browser.find_element_by_xpath(".//*[@id='global-nav']/div/div/span/a[1]")
            jumplogin.click()
            #多层窗口定位，切换到弹出的登录页面
            browser.switch_to.frame('J_login_iframe')
            #获取用户名 密码 登录按钮
            loginname = browser.find_element_by_xpath(".//*[@id='username']")
            password = browser.find_element_by_xpath(".//*[@id='password']")
            submit = browser.find_element_by_xpath(".//*[@id='login_submit']")
            loginname.send_keys(myusername)
            time.sleep(1)
            password.send_keys(mypassword)
            time.sleep(1)
            submit.click()
            time.sleep(2)
            print u'用户%d登陆成功' % (a)
            time.sleep(2)
            #判断是否已经签到，没有签到的话进行签到
            signsubmit = browser.find_element_by_xpath(".//*[@id='index-head']/div[3]/div[2]/a")
            if u'已签到' in signsubmit.text:
                print u'用户%d已签到' % (a)
            else:
                signsubmit.click()
                time.sleep(2)
                if u'已签到' in signsubmit.text:
                    print u'用户%d签到成功' % (a)
            time.sleep(5)
    except:
        traceback.print_exc()
        print 'Failed'

    browser.quit()
    #签到成功，进入下一次
    a = a+1

