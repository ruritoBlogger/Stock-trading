# coding: UTF-8
import pandas as pd
import csv
import re
import numpy as np

#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)
f = open('nikkei.txt','a')
def getStockdata():
    f = open('get_2018_nikkeiheikin_stock_data.txt')
    lines = f.readlines()

    t = 0
    correct = 0
    false = 0
    num = 0
    start = 0
    last = 0
    flag = False
    next_num = 0
    brand_num = 0

    for line in lines:
        n = 0
    
        if(line[n] == " "):
            flag = True
            continue

        if(flag):
            flag = False
            tmp = line.rstrip('\n')
            tmp = tmp.rstrip('')
            tmp = tmp.replace('"', '')
            while(True):
                if(n == len(str(tmp))):
                    break
                if(tmp[n] == "\n"):
                    break
                n += 1
            if(t == 0):
                t = int(float(tmp[num:n]))
            
            if(t == int(float(tmp[num:n])) ):
                continue
            print(t)
            f.write(str(t))
            t = 0
            continue
getStockdata()
