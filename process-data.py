# 数据存储文件夹  /data/
# eg /data/tran_train.csv
# from sklearn.metrics import roc_auc_score
import pandas as pd
from datetime import datetime
# import numpy as np

acct_train=pd.read_csv("/data/acct_train.csv")
cust_train=pd.read_csv("/data/cust_train.csv")
tran_train=pd.read_csv("/data/tran_train.csv")
cards_train=pd.read_csv("/data/cards_train.csv")
acct_test=pd.read_csv("/data/acct_test.csv")
tran_test=pd.read_csv("/data/tran_test.csv")
cards_test=pd.read_csv("/data/cards_test.csv")

#处理训练数据集部分,并生成训练数据集
data=pd.DataFrame(acct_train)
# 删除acct_train的两行脏数据
data=data.drop(index=568)
data=data.drop(index=862)
data.index=range(len(data))
x_cat1=data['x_cat1']
x_num1=data['x_num1']
label=data['label']

tran_train=tran_train.fillna(0)
train_x_num1=tran_train['x_num1']
train_x_num2=tran_train['x_num2']
train_x_num3=tran_train['x_num3']
train_x_num4=tran_train['x_num4']
train_x_num5=tran_train['x_num5']
train_x_num6=tran_train['x_num6']
train_x_num7=tran_train['x_num7']
train_x_num8=tran_train['x_num8']
train_x_num9=tran_train['x_num9']
train_x_num10=tran_train['x_num10']
train_x_num11=tran_train['x_num11']
train_x_num12=tran_train['x_num12']
train_x_num13=tran_train['x_num13']
train_x_num14=tran_train['x_num14']
train_x_num15=tran_train['x_num15']
train_x_num16=tran_train['x_num16']
train_x_num17=tran_train['x_num17']
train_x_num18=tran_train['x_num18']
train_x_num19=tran_train['x_num19']
train_x_num20=tran_train['x_num20']
train_x_num21=tran_train['x_num21']
train_x_num22=tran_train['x_num22']
train_x_num23=tran_train['x_num23']


cards_data=pd.DataFrame(cards_train)
cards_data=cards_data.drop(index=568)
cards_data=cards_data.drop(index=862)
cards_data.index=range(len(cards_data))
cards_x_cat2=cards_data['x_cat2']
x_date1=cards_data['x_date1']
times=[]
for i in range(0,len(x_date1)):
    time = x_date1[i]
    temp = datetime.fromisoformat(time).timestamp()
    times.append(temp)

res={"x_cat1": x_cat1, "x_num1": x_num1, "train_x_num1": train_x_num1, "train_x_num2": train_x_num2,
       "train_x_num3": train_x_num3, "train_x_num4": train_x_num4, "train_x_num5": train_x_num5,
       "train_x_num6": train_x_num6, "train_x_num7": train_x_num7, "train_x_num8": train_x_num8,
       "train_x_num9": train_x_num9, "train_x_num10": train_x_num10, "train_x_num11": train_x_num11,
       "train_x_num12": train_x_num12, "train_x_num13": train_x_num13, "train_x_num14": train_x_num14,
       "train_x_num15": train_x_num15, "train_x_num16": train_x_num16, "train_x_num17": train_x_num17,
       "train_x_num18": train_x_num18, "train_x_num19": train_x_num19, "train_x_num20": train_x_num20,
       "train_x_num21": train_x_num21, "train_x_num22": train_x_num22, "train_x_num23": train_x_num23,
       "cards_x_cat2": cards_x_cat2, "cards_x_date1": times,
       "label": label}

res_data=pd.DataFrame(res)
res_data.to_csv("./data_train10.csv", index=0)

# data=pd.read_csv("./data_train10.csv")
# print(data)

