# coding: UTF-8
import pandas as pd
import csv
import re
import numpy as np

#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)
fil= open('nikkei.txt','a')

def getStockdata():
    f = open('get_2018_nikkeiheikin_stock_data.txt')
    lines = f.readlines()

    correct = 0
    false = 0
    num = 0
    start = 0
    last = 0
    flag = False
    next_num = 0
    brand_num = 0
    t = 0

    for line in lines:
        n = 0
    
        if(line[n] == " "):
            flag = True
            if(brand_num == 0):
                brand_num = next_num
                continue
            print(brand_num)
            if(t == 0):
                fil.write(str(brand_num)+"\n")
                t = brand_num
            if(t == brand_num):
                brand_num = next_num
                continue
            else:
                fil.write(str(brand_num)+"\n")
                t = brand_num
                
            brand_num = next_num
            continue

        tmp = line.rstrip('\n')
        tmp = tmp.rstrip('')
        tmp = tmp.replace('"', '')
        if(len(tmp) == 0):
            continue

        while(True):
            if(n == len(tmp)):
                break
            if(tmp[n] == "\n"):
                break
            n += 1

        last = next_num
        next_num = int(float(tmp[num:n]))
        if(flag):
            start = int(float(tmp[num:n]))
            flag = False

getStockdata()
