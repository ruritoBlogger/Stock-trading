#coding=UTF-8

import urllib2
from bs4 import BeautifulSoup

#アクセスするurl
url = "http://www.rcc.ritsumei.ac.jp/?page_id=8895"

# urlにアクセスした時の返り値
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

print(soup.find_all('#post-8895 > div > tbody'))
