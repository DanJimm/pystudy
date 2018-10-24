# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome() #打开一个浏览器
#browser.maximize_window() #最大化
driver.implicitly_wait(8) #隐士等待

url = "https://www.baidu.com"
driver.get(url)

driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()  #点击百度一下按钮

time.sleep(2)

if driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed():
    print u'搜索成功'
else:
    print u'搜索失败'
driver.quit()