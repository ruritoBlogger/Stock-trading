# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import re

# アクセスするURL
url = "http://joujou.skr.jp/mothers/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

f = open('mothers.txt','a')

count = False
n = 2
while(True):
    
    #強制終了
    if n == 285:
        break

    if soup.select_one("#HPB_TABLE_4_A_180210131757 > tbody > tr:nth-of-type(" + str(n) + ") > td:nth-of-type(3)") == None:
        if count == True:
            break
        else:
            count = True
            n += 1
            continue
    target = soup.select_one("#HPB_TABLE_4_A_180210131757 > tbody > tr:nth-of-type(" + str(n) + ") > td:nth-of-type(3)").string
    #print(soup.select_one("#HPB_TABLE_4_A_180210131757 > tbody > tr:nth-of-type(" + str(n) + ") > td:nth-of-type(3)").string)
    
    print(target)
    n += 1;
    count = False

    f.write( target + '\n')

f.close()
