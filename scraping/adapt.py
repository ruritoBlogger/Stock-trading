# coding: UTF-8
import pandas as pd


f = open('.txt','a')

df = pd.DataFrame( columns = ["銘柄番号","終値"] )

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
    tmp_list = pd.Series( [brand_num,next_num] )
    print(tmp_list)
    df = df.append(tmp_list, ignore_index=True)
    if(flag):
        start = int(float(tmp[num:n]))
        flag = False

f.close()
df.to_csv("test.csv")
