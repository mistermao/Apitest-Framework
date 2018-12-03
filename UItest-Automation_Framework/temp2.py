# !/usr/bin/python3
import time
from selenium import webdriver
import os
import configparser

drive = webdriver.Firefox()
drive.maximize_window()
drive.implicitly_wait(5)
drive.get("http://ehrtest.source3g.com/h5/birthday/birthday.html")
drive.find_element_by_xpath(".//*[@id='app']/div/form/div[1]/div/div[1]/input").send_keys("GS0415")
drive.find_element_by_xpath(".//*[@id='app']/div/form/div[3]/div/div/input").click()
drive.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[6]/div/span").click()
drive.find_element_by_xpath("//*[@id='app']/div/form/div[4]/div/div/span[2]/span").click()
drive.find_element_by_xpath(".//*[@id='app']/div/form/div[6]/div/button[2]").click()
drive.quit()


