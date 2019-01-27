# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ブラウザを起動する
driver = webdriver.Chrome(executable_path='/home/rurito/chromedriver')

#Mothersの株の情報を持ってくる

f = open('mothers.txt')
lines = f.readlines()

#mothersの銘柄番号が格納されている配列を回す
for line in lines:
    #なぜか空白が抜けてない
    line = line.replace(u"	","")
    # アクセスするURL
    driver.get("https://shikiho.jp/stocks/" + line + "/")

    #url = "https://shikiho.jp/stocks/" + "2121" + "/"
    
    # HTMLを文字コードをUTF-8に変換してから取得します。
    html = driver.page_source.encode('utf-8')

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    #target = soup.select_one("#main > div:nth-of-type(1)")
    #target = soup.select_one("#main > div > div.overview.cfx > div.main > div.title > div > div.name > div")
    #target = soup.select_one("#main > div > div.section > div:nth-of-type(1) > div.main > div > div.performance > div.matrix > table > tbody > tr:nth-of-type(1)")
       
    target = soup.find_all("div")

    for mark in target:
        if not mark.find_all(class_="table") == None:
            print(mark.find_all(class_="table")

f.close()
