# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from stock import Stock

driver = webdriver.Chrome(executable_path='/home/rurito/chromedriver')
#初回起動は時間がかかるので予め起動
driver.get("https://shikiho.jp/stocks/2121")
time.sleep(2)

#マザーズの銘柄番号を取得する
f = open('mothers.txt')
lines = f.readlines()
label = ["売上高","営業利益","経常利益","純利益","1株益","1株配"]

#取得した銘柄番号を用いて業績を取り出す
for line in lines:
    #空白抜き
    line = line.replace(u"	","")
    driver.get("https://shikiho.jp/stocks/" + line + "/")
    time.sleep(1) #magic number

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    brand_name = soup.select_one("#main > div > div.overview.cfx > div.main > div.title > div > div.name > div").text
    stock = Stock(line,brand_name)
    #b = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
    
    for i in range(10):
        year = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(" + str(i + 1) + ") > td:nth-of-type(1)")
        for j in range(6):
            data = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(" + str(i + 1) + ") > td:nth-of-type(" + str(j + 2) + ")")
            if data is None:
                break
            #print(data.text)
            print(data.text)
            stock.setData(year.text,label[j],data.text)
    stock.output()
f.close()
