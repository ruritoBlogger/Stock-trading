# coding: UTF-8

class Stock:
    def __init__(self,brand_num,brand_name):
        self.brand_num = brand_num
        self.brand_name = brand_name

    #業績を保存
    def setData(self,time,data_type,data):
        self.data[time][data_type] = data

    #データの出力
    def output(self):
        print(self.brand_name)
        print(self.brand_num)
        for list in self.data:
            for data in list:
                print(data)



