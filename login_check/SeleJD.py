#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #导入鼠标操作
from selenium.webdriver.common.keys import Keys #导入键值操作
import time
import traceback

myusername = '17341375202' #设置账号
mypassword = 'yx19920411' #设置密码
signpage = 'http://vip.jd.com/home.html' #JD签到登录页

browser = webdriver.Chrome() #初始化浏览器对象
#browser.maximize_window() #浏览器最大

try:
    browser.get(signpage) #打开登录页面
    #browser.implicitly_wait(5)

    #切换到账户登录
    jumplogin = browser.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]/div/div[3]/a")

    #获取用户名 密码 登录按钮
    loginname = browser.find_element_by_xpath(".//*[@id='loginname']")
    password = browser.find_element_by_xpath(".//*[@id='nloginpwd']")
    submit = browser.find_element_by_xpath(".//*[@id='loginsubmit']")

    jumplogin.click()

    loginname.send_keys(myusername)
    time.sleep(1)
    password.send_keys(mypassword)
    time.sleep(1)
    submit.click()
    time.sleep(1)

except:
    traceback.print_exc()
    print 'Failed'


browser.quit()