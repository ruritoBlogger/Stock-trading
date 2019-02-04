# coding: UTF-8
import pandas as pd
import csv
import re

#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)

def getStockdata(key,per):
    f = open('get_2018_mothers_stock_data.txt')
    lines = f.readlines()

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
            if(brand_num != key):
                brand_num = next_num
                continue
            else:
                print("start is  "+str(start))
                print("last is  "+ str(last))
                print("brand_num  is  "+ str(brand_num))
                print("per  is  "+ str(per))
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
        next_num = int(tmp[num:n])
        if(flag):
            start = int(tmp[num:n])
            flag = False

with open('test.csv','r',newline='',encoding='utf-8') as f:

    r = csv.reader(f)
    
    pattern = r"予"
    target = r"連"
    flag = True
    n = 1
    for l in r:
        #print(l[1].rstrip('\n')+"番の企業の"+l[3]+"の時期のPERは"+l[8])
        #tmp = l[3]
        #tmp2 = re.compile(pattern)
        #result = tmp2.match(tmp)
        #print(result)
        #print(l[3][n-1])
        if(flag):
            flag = False
            continue
        if(l[8] == "--"):
            continue
        if(l[3][n-1] != "連"):
            continue
        #print(l[3][n+1])
        if(l[3][n+1] != "8"):
            continue
        #elif(l[8][0] = "-"):
            #continue
        #print(l)

        getStockdata(float(l[1]),float(l[8]))

        print(l[1].rstrip('\n')+"番の企業の"+l[3]+"の時期のPERは"+l[8])



