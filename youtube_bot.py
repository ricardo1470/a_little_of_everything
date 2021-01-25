#!/usr/bin/python3
""" script that generates
    views on youtube """


from selenium import webdriver
import time
from random import randrange


time_view = 5
list_browser = []

browser_1 = webdriver.Chrome(executable_path='./chromedriver')
browser_2 = webdriver.Chrome(executable_path='./chromedriver')
browser_3 = webdriver.Chrome(executable_path='./chromedriver')
browser_4 = webdriver.Chrome(executable_path='./chromedriver')

list_browser.append(browser_1)
list_browser.append(browser_2)
list_browser.append(browser_3)
list_browser.append(browser_4)

for browser in list_browser:
    """ url you want to visit """
    browser.get('https://www.youtube.com/watch?v=9GQ5AgZqN3Y&t=15s')

while(True):
    number_random = randrange(0, len(list_browser))
    list_browser[number_random].refresh()
    print("browser number: ", number_random, "has been updated")
    time.sleep(time_view)
