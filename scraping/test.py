# coding: UTF-8

f = open('get_2018_mothers_stock_data.txt')
lines = f.readlines()

i = 0
num = 0
start = 0
last = 0
flag = False
next_num = 0
brand_num = 0
for line in lines:
    n = 0
    #if(i == 300):
        #break
    #print(line[n-1])
    #print(line)
    
    if(line[n] == " "):
        flag = True
        print("start is  "+str(start))
        print("last is  "+ str(last))
        print("brand_num  is  "+ str(brand_num))
        brand_num = next_num
        i += 1
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
    #print(int(tmp[num:n]))
    last = next_num
    next_num = int(tmp[num:n])
    if(flag):
        start = int(tmp[num:n])
        flag = False
    i += 1
