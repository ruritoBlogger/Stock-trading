#coding=UTF-8

import urllib2
from bs4 import BeautifulSoup

#アクセスするurl
url = "http://daioh.dengeki.com/taisho/yagate/"

# urlにアクセスした時の返り値
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 小タイトルを取得
title = soup.select_one('#story')
print(title.string)

# あらすじを取得
arasuzi = soup.select_one('#storyTxt')
arasuzi.br.unwrap()
print(arasuzi)
