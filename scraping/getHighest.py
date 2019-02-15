# coding: UTF-8
import pandas as pd
import csv
import re
import numpy as np

#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)

def getStockdata(key,per,percent):
    f = open('get_2018_mothers_stock_data.txt')
    lines = f.readlines()

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
            if(brand_num != key):
                brand_num = next_num
                continue
            else:
                if(percent == 0):
                    continue
                per = start / per
                if(start < last):
                    #print("per  is  "+ str(per) + "  and  stock data uped")
                    if(per < percent):
                        return 1
                    else:
                        return 2
                else:
                    return 0
                    #print("per  is  "+ str(per) + "  and  stock data downed")
                    #if(per > percent):
                        #return True
                    #else:
                        #return False
                #print("start is  "+str(start))
                #print("last is  "+ str(last))
                #print("brand_num  is  "+ str(brand_num))
                #print("per  is  "+ str(per))
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

def check_per(key):

    with open('test.csv','r',newline='',encoding='utf-8') as f:

        r = csv.reader(f)
    
        correct = 0
        false = 0
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
            #print(l)

            if(getStockdata(float(l[1]),float(l[8]),key) == 1):
                correct += 1
            elif(getStockdata(float(l[1]),float(l[8]),key) == 2):
                false += 1

            #print(l[1].rstrip('\n')+"番の企業の"+l[3]+"の時期のPERは"+l[8])

    #print("correct  is  "+ str(correct) + "  and false  is  "+ str(false))
    #print("%  is  " + str(correct / (correct + false)) )
    if(correct + false == 0):
        return 0
    return correct / (correct + false)

match_point = 0
goodest = 0
key_per = 0
for key in np.arange(130,400,5):
    match_point = check_per(key)
    print("match_point  is  "+ str(match_point) + "  and  percent  is  "+ str(key) )
    if(goodest < match_point):
        goodest = match_point
        key_per = key

print("This is a result")
print("best  match_point  is  " + str(goodest) + "  at  "+ str(key_per))
