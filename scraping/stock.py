# coding: UTF-8

class Stock:
    def __init__(self,brand_num,brand_name):
        self.brand_num = brand_num
        self.brand_name = brand_name
        self.data = {}

    #業績を保存
    def setData(self,time,data_type,num_data):
        #self.data[time][int(data_type)] = data
        #self.data.setdefault(time,[]).setdefault(data_type,[]).append(data)
        label = ["売上高","営業利益","経常利益","純利益","1株益","1株配"]
        time = time.encode('utf-8')
        print(type(time))
        print(time)
        self.data = dict(time=num_data)

    #データの出力
    def output(self):
        print(self.brand_name)
        print(self.brand_num)
        print(self.data)
        for list in self.data:
            print(list)
