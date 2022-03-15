import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import torch
data = pd.read_csv('./data_train10.csv')
data.head()
data_test = pd.read_csv('./data_test10.csv')

X_res = data_test.iloc[:, 0:27]

X = data.iloc[:, 0:27]
Y = data.iloc[:, 27]

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

lgb_train = lgb.Dataset(X_train, Y_train)
lgb_eval = lgb.Dataset(X_test, Y_test, reference=lgb_train)

params = {
    'task': 'train',
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'regression',  # 目标函数
    'metric': {'l2', 'auc'},  # 评估函数
    'num_leaves': 80,  # 叶子节点数
    'learning_rate': 0.005,  # 学习速率
    'feature_fraction': 0.9,  # 建树的特征选择比例
    'bagging_fraction': 0.8,  # 建树的样本采样比例
    'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
    'verbose': 1  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
}

# 模型训练
gbm = lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval, early_stopping_rounds=5)

# 模型保存
gbm.save_model('model.txt')

# 模型加载
gbm = lgb.Booster(model_file='model.txt')

# 模型预测
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)

# 模型评估
print('The rmse of prediction is:', mean_squared_error(Y_test, y_pred) ** 0.5)

y_res = gbm.predict(X_res, num_iteration=gbm.best_iteration)

cards = pd.read_csv("/data/acct_test.csv")
cards1 = cards['卡号']
res = {"卡号": cards1, "target": y_res}
res1 = pd.DataFrame(res)
res1.to_csv("./pre_result.csv", index=0)
print("finish")


