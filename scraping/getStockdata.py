# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from stock import Stock
import pandas as pd

driver = webdriver.Chrome(executable_path='/home/rurito/chromedriver')
#初回起動は時間がかかるので予め起動
driver.get("https://shikiho.jp/stocks/2121")
time.sleep(2)

#マザーズの銘柄番号を取得する
f = open('mothers_stock_number.txt')
lines = f.readlines()
label = ["売上高","営業利益","経常利益","純利益","1株益","1株配"]

df = pd.DataFrame( columns = ["銘柄番号","企業名","時期","売上高","営業利益","経常利益","純利益","1株益","1株配"] ) 


#取得した銘柄番号を用いて業績を取り出す
for line in lines:

    #空白抜き
    line = line.replace(u"	","")
    driver.get("https://shikiho.jp/stocks/" + line + "/")
    time.sleep(1) #magic number

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    brand_name = soup.select_one("#main > div > div.overview.cfx > div.main > div.title > div > div.name > div")
    #stock = Stock(line,brand_name)
    #b = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
    if brand_name is None:
        continue
    brand_name = brand_name.text
    print(brand_name)
    
    for i in range(10):
        array = []
        year = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(" + str(i + 1) + ") > td:nth-of-type(1)")
        if year is None:
            continue
        print(year.text)
        year = year.text
        for j in range(6):
            data = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(" + str(i + 1) + ") > td:nth-of-type(" + str(j + 2) + ")")
            if data is None:
                break
            #stock.setData(year.text,j,data.text)
            array.append(data.text)
        print(array)

        tmp = pd.Series( [line.encode('utf-8'),brand_name.encode('utf-8'),year.encode('utf-8'),array[0].encode('utf-8'),array[1].encode('utf-8'),array[2].encode('utf-8'),array[3].encode('utf-8'),array[4].encode('utf-8'),array[5].encode('utf-8')], index = df.columns)
        df = df.append(tmp, ignore_index=True)
    #stock.output()
f.close()
df.to_csv("test.csv")
