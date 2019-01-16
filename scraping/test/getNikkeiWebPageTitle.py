#coding=UTF-8

import urllib2
from bs4 import BeautifulSoup

#アクセスするurl
url = "http://www.nikkei.com/"

# urlにアクセスした時の返り値
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトル要素を取得
title_tag = soup.title

# 要素の文字列を取得する
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを出力
print(title)
