# coding: UTF-8

class Stock:
    def __init__(self,brand_num,brand_name):
        self.brand_num = brand_num
        self.brand_name = brand_name
        self.data = {}

    #業績を保存
    def setData(self,time,data_type,data):
        #self.data[time][int(data_type)] = data
        #self.data.setdefault(time,[]).setdefault(data_type,[]).append(data)
        tmp = {data_type.decode('unicode-escape') : data.decode('unicode-escape')}
        print(tmp)
        self.data[time].append(tmp)

    #データの出力
    def output(self):
        print(self.brand_name)
        print(self.brand_num)
        #print(self.data)
        for list in self.data:
            print(data)
