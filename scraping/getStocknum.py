# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(executable_path='/home/rurito/chromedriver')
#初回起動は時間がかかるので予め起動
driver.get("https://kabuoji3.com/stock/2121/2018/")
time.sleep(2)

#マザーズの銘柄番号を取得する
f = open('mothers.txt')
lines = f.readlines()

out = open("stock_num.txt","a")

for line in lines:
    
    #空白抜き
    line = line.replace(u"	","")
    driver.get("https://kabuoji3.com/stock/" + line + "/2018/")
    time.sleep(1) #magic number
 
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    name = soup.select_one("#base_box > header > h2 > span.jp")
    if name is None:
        continue
    name = name.text.encode('utf-8'),
    print(type(name))
    out.write( name)
    
    for i in range(500):
        target = soup.select_one("#base_box > div > div.data_contents > div > div > div > table > tbody:nth-of-type(" + str(i + 1) + ") > tr > td:nth-of-type(5)")
        if target is None:
            continue
        target = target.text.encode('utf-8'),
        out.write(target)
        print(target)

out.close()
