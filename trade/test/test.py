#coding=utf-8
import pandas as pd

df = pd.read_csv("4307_2018.csv",encoding='Shift_JIS')

for line in df:
    print(line)
