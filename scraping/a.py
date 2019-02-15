# coding: UTF-8
import pandas as pd
import csv
import re
import numpy as np

#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)

def getStockdata(key,per,percent):
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

    for line in lines:
        n = 0
    
        if(line[n] == " "):
            flag = True
            if(brand_num != int(key)):
                brand_num = next_num
                continue
            else:
                per = start / per
                if(start < last):
                        return 1
                else:
                    return 2
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
        next_num = int(float(tmp[num:n]))
        if(flag):
            start = int(float(tmp[num:n]))
            flag = False

def check_percent(key,num,per):

    tmp = 0
    tmp_data = 0
    
    with open('nikkei.csv','r',newline='',encoding='utf-8') as f:

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
            if(l[3][n-1] != "連"):
                tmp = 0
                continue

            tmp = int(l[3][n+1])


                
            if(tmp == 6):
                if(l[7].replace(',','.').replace('‥','') == "--"):
                    continue
                tmp_brand = int(l[1])
                tmp_data = float(l[7].replace(',','.').replace('‥',''))
                tmp_flag = True
            
            elif(tmp == 7):
                if(l[7].replace(',','.').replace('‥','') == "--"):
                    tmp_flag = False
                    continue
                if(tmp_flag and tmp_brand == int(l[1]) and tmp_data - tmp_data/(num * per) < float(l[7].replace(',','.').replace('‥','')) ):
                    tmp_data = float(l[7].replace(',','.').replace('‥',''))
                else:
                    tmp_flag = False

            elif(tmp == 8):
                if(l[7].replace(',','.').replace('‥','') == "--"):
                    tmp_flag = False
                    continue
                if(tmp_flag and tmp_brand == int(l[1]) and tmp_data - tmp_data/ (num * (1 - per)) < float(l[7].replace(',','.').replace('‥','')) ):
                    if(getStockdata(int(l[1]),float(l[8].replace(',','.').replace('‥','')),key) == 1):
                        correct += 1
                    elif(getStockdata(int(l[1]),float(l[8].replace(',','.').replace('‥','')),key) == 2):
                        false += 1
                tmp_flag = False
            #print(l[1].rstrip('\n')+"番の企業の"+l[3]+"の時期のPERは"+l[8])

    #print("correct  is  "+ str(correct) + "  and false  is  "+ str(false))
    #print("%  is  " + str(correct / (correct + false)) )
    if(correct + false == 0):
        return 0
    return correct / (correct + false)

match_point = 0
goodest = 0
key_per = 0
#for key in np.arange(5,200,5):
#print("match_point  is  "+ str(match_point) + "  and  percent  is  "+ str(key) )
for i in np.arange(2.0,4.0,0.1):
    for j in np.arange(0.1,0.5,0.1):
        match_point = check_percent(15,i,j)
        print("match_point  is  "+ str(match_point) + "  at  key_a  is  "+ str(i) + "  and  key_per  is  "+str(j))
        if(goodest < match_point):
            goodest = match_point
            key_a = i
            key_per = j

print("This is a result")
print("best  match_point  is  " + str(goodest) + "  at  key_a  is  "+ str(key_a) + "  and  key_per  is  "+str(key_per))
