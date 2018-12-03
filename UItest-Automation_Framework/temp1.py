# !/usr/bin/python3
import time
from selenium import webdriver
import os
import configparser

config = configparser.ConfigParser()
dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
print(dir)
file_path = os.path.dirname(os.path.abspath('.')) + '/config/empcode.txt'
print(file_path)
with open(file_path, "r") as foo:
    for line in foo.readlines():
        line = line.rstrip("\n")
        print(line)
        drive = webdriver.Firefox()
        drive.set_window_size(600, 800)
        drive.implicitly_wait(5)
        drive.get("http://ehrtest.source3g.com/h5/birthday/birthday.html")
        drive.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input").send_keys(line)
        drive.find_element_by_xpath(".//*[@id='app']/div/form/div[3]/div/div/input").click()
        drive.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[3]/div/span").click()
        drive.find_element_by_xpath("//*[@id='app']/div/form/div[4]/div/div/span[2]/span").click()
        drive.find_element_by_xpath(".//*[@id='app']/div/form/div[6]/div/button[2]").click()
        drive.quit()



