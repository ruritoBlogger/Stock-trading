# coding: UTF-8
import pandas as pd
import csv
import re

#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)

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
        print(float(l[8]))
        #elif(l[8][0] = "-"):
            #continue
        #print(l)

        print(l[1].rstrip('\n')+"番の企業の"+l[3]+"の時期のPERは"+l[8])
