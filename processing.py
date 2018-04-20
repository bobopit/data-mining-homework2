import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter

filename = './dataset/Building_Permits.csv'
# f=open(filename)
# reader = csv.DictReader(f)
#
# attribute=[]
# for row in reader:
#     for item in list(row):
#         attribute.append(item)
#     break
# print attribute
#
#
# f.close()
#
#
#
# for i in range(0,len(attribute)):
#     new_li = []
#     f = open(filename)
#     reader = csv.DictReader(f)
#     for row in reader:
#         # print row
#         if row[attribute[i]] not in new_li:
#             new_li.append(row[attribute[i]])
#         # count[row[attribute[i]]] = count.setdefault(row[attribute[i]], 0)
#     print attribute[i],len(new_li)
#     f.close()
#         # count[row["Permit Type Definition"]] += 1


#
# attribute=[]
# # df=pd.DataFrame(pd.read_csv(filename))
# df=pd.read_csv(filename)
#
# row = df.columns.size
#
# for i in range(row):
#     n = df.icol(i).value_counts()
#     print n

# for attr in df.columns:
#     x = df[attr]
#     n = x.value_counts()
#     if n.count() <= 100:
#         attribute.append(attr)
#         print attr,n.count()
#
#
# df=df[attribute]
# df.to_csv("./dataset/test.csv",index=False)
#
# df=pd.read_csv("./dataset/test.csv")
# print df

# coding=utf-8
import pandas as pd

obj = pd.read_csv("./dataset/Building_Permits.csv")
attr=[]

for item in obj.columns:
    n = obj[item].value_counts()
    if n.count() < =50:
        attr.append(item)
        print item,n.count()

df = obj[attr]
df.to_csv("./dataset/test.csv",index=False)
