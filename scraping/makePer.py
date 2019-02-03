# coding: UTF-8
import pandas as pd
import csv
#df = pd.read_csv("test.csv")

#for line in df:
    #print(line)

with open('test.csv','r',newline='',encoding='utf-8') as f:

    r = csv.reader(f)

    for l in r:
        print(l[1]+"番の企業の"+l[3]+"の時期のPERは"+l[8])
        #print(l)
