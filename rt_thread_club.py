#-*- coding:utf8 -*-
import os
import sys
import time
import logging
from selenium import webdriver


def login_in_club(user_name, pass_word):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=option)

    # login in
    driver.get("https://www.rt-thread.org/account/user/index.html?response_type=code&authorized=yes&scope=basic&state=1588816557615&client_id=30792375&redirect_uri=https://club.rt-thread.org/index/user/login.html")

    driver.find_element_by_id("username").click()
    driver.find_element_by_id('username').clear()
    time.sleep(1)
    driver.find_element_by_id('username').send_keys(user_name)
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').clear()
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(pass_word)
    driver.find_element_by_id('login').click()

    time.sleep(10)
    try:
        element = driver.find_element_by_link_text(u"立即签到")
    except Exception as e:
        logging.error("Error message : {0}".format(e))
    else:
        element.click()
        logging.info("sign in success!")

    time.sleep(1)
    
    day_num = None
    # check sign in days
    try:
        element = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]")
    except Exception as e:
        logging.error("Error message : {0}".format(e))
    else:
        day_num = element.text
        logging.info("signed in today : {0}".format(day_num))
        driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/h3[1]/div[1]/a[1]').click()
        driver.get_screenshot_as_file("paihang.jpg")
        driver.quit()
    return day_num
