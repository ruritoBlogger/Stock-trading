# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path='/home/rurito/chromedriver')

f = open('mothers.txt')
lines = f.readlines()

for line in lines:
    line = line.replace(u"	","")
    driver.get("https://shikiho.jp/stocks/" + line + "/")
    time.sleep(3)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    target = soup.find_all("div", class_="table")
    for mark in target:
        print(mark.text)
f.close()
