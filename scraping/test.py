# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path='/home/rurito/chromedriver')
#初回起動は時間がかかるので予め起動
driver.get("https://shikiho.jp/stocks/2121")
time.sleep(2)

#マザーズの銘柄番号を取得する
f = open('mothers.txt')
lines = f.readlines()

#取得した銘柄番号を用いて社名を取り出す
for line in lines:
    line = line.replace(u"	","")
    driver.get("https://shikiho.jp/stocks/" + line + "/")
    time.sleep(0.7) #magic number
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    a = soup.select_one("#main > div > div.overview.cfx > div.main > div.title > div > div.name > div").text
    print(a)
    #target = soup.find_all("div", class_="table")
    #for mark in target:
        #print(mark.text)
f.close()
