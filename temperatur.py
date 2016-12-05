# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#use username password of the account, and enter the url
user = ""
passw = ""
url = ""

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("password").send_keys(passw)
driver.save_screenshot("verification.jpg")
time.sleep(16)
verificationcode = input("enter the verification code: ")
driver.find_element_by_id("textyz").send_keys(verificationcode)
subm = driver.find_element_by_xpath('//*[@id="button"]')
subm.send_keys(Keys.ENTER)
zhijian = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[3]/td[1]/a/img')
zhijian.click()
lurujiemian = driver.find_element_by_xpath('//*[@id="btn_begin"]')
lurujiemian.send_keys(Keys.ENTER)
wenduluru = driver.find_element_by_xpath('//*[@id="tab_nr"]/ul[1]/div/table/tbody/tr/td[2]/input')
wenduluru.click()

oldtab = driver.current_window_handle
alltab = driver.window_handles

for handle in alltab:
    if handle != oldtab:
        driver.switch_to_window(handle)
        break

lurudata = driver.find_element_by_xpath('//*[@id="dt"]/tbody/tr[22]/td/a')
lurudata.click()
#以下数据是录入数据需要调用的element和xpath
录入数据的id(dkhvalue,clsjvalue, wdvalue, sdvalue)
确定按钮xpath（//*[@id="input_Wsd"]/div/table/tbody/tr[6]/th/input[1]）
#test comment
