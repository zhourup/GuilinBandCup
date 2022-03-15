# GuilinBankCup
桂林银行杯(初赛12，复赛19)

**1、赛题分析**

基于业务场景下脱敏数据，运用统计或机器学习等算法，预测该卡欺诈风险。由此可知，我们需要建立模型，然后使用赛题给定的四个训练数据集训练模型。最后将根据给定的四个测试数据集，预测数据集中每个卡号受到欺诈风险的概率。

**2、数据集分析**

一共给定了八个数据集，分别是四个训练数据集和四个测试数据集，测试数据集相比训练数据集缺少了label列(在acct_test.csv中)，即待预测列。所以需要将四个数据集按卡号为id合并成一个数据集。

**脏数据**：通过输出四个训练数据集发现，acct_train.csv和cards_train.csv有8376行(包含列名),而train_train.csv只有8374行数据，若想将它们合并成一个数据集，需将acct_train.csv 和cards_train.csv中的多余行给删除掉，通过代码比较三个数据集发现，acct_train.csv和cards_train.csv中的卡号为519562和529914的对应行数据在train_train是没有的，所以在处理训练数据集中得将这两行数据给剔除掉，以免造成数据误差。

**3、模型选取**

选取LightGBM模型，除此之外，还使用了线性回归、逻辑回归、k-means、knn、mlp(多层感知机)进行训练，但LightGBM效果最优。

**4、流程**

![img](https://github.com/zhourup/GuilinBankCup/blob/main/img.png)

