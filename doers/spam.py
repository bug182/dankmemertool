from importlib import reload
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import doers.config 
import time
import os



class beg:
    def __init__(self):
        os.system('cls')
        config = reload(doers.config)
        print('opening window and loging in')
        self.driver = webdriver.Firefox(executable_path=r".//doers//geckodriver.exe")
        self.driver.get(config.channel)
        self.emailB = self.driver.find_element_by_xpath("//input[@type='email']")
        self.psswrd = self.driver.find_element_by_xpath("//input[@type='password']")
        self.emailB.send_keys(config.email)
        self.psswrd.send_keys(config.password, Keys.ENTER)
        time.sleep(6)
        print('starting to beg every ' + str(config.beg_time) + ' seconds')
        self.send_msg()

    def wait_time(self):
        time.sleep(config.beg_time)
        self.send_msg()

    def send_msg(self):
        self.msg_box = self.driver.find_element_by_tag_name('textarea')
        self.msg_box.send_keys("pls beg", Keys.ENTER)
        print('sent beg')
        self.wait_time()


class gamble:
    def __init__(self):
        os.system('cls')
        config = reload(doers.config)
        plrint('opening window and loging in')
        self.driver = webdriver.Firefox(executable_path=r".//doers//geckodriver.exe")
        self.driver.get(config.channel)
        self.emailB = self.driver.find_element_by_xpath("//input[@type='email']")
        self.psswrd = self.driver.find_element_by_xpath("//input[@type='password']")
        self.emailB.send_keys(config.email)
        self.psswrd.send_keys(config.password, Keys.ENTER)
        time.sleep(6)
        print('starting to gamble with ' + str(config.gamble_amount) + ' coins, every ' + str(config.gamble_time) +  'seconds')
        self.send_msg()

    def wait_time(self):
        time.sleep(config.gamble_time)
        self.send_msg()

    def send_msg(self):
        self.msg_box = self.driver.find_element_by_tag_name('textarea')
        self.msg_box.send_keys("pls gamble " + str(config.gamble_amount), Keys.ENTER)
        print('sent gamble')
        self.wait_time()