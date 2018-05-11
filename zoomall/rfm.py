# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd

fArr = [
    open('2月订单明细.csv', encoding='ansi'),
    open('3月订单明细.csv', encoding='ansi'),
    open('4月订单明细.csv', encoding='ansi'),
]
custom_key = '联系手机'
use_cols = ['买家会员名', custom_key, '订单创建时间', '买家实际支付金额']
dataArr = []
for f in fArr:
    data = pd.read_csv(
        f,
        # header=0,  # 指定行为列名。默认为0表示第一行为列名，如果为None则使用索引数字号表示列名(如:0,1,2)
        # index_col='买家会员名',  # 指定列为索引
        # skiprows=[2, 4],  # 忽略指定的行
        usecols=use_cols,  # 指定使用的列数据
        # encoding='ansi'  # 指定文件的编码格式
    )
    data = data[data['买家实际支付金额'] > 0]  # 数据过滤
    dataArr.append(data)
dataAll = pd.concat(dataArr)  # 纵向合并数据

# 计算交易时间距离现在的天数
dataAll['dataDiff'] = (pd.to_datetime('now')-pd.to_datetime(dataAll['订单创建时间'])).dt.days

# 计算R值(每个客户距离现在最近的天数)
R_agg = dataAll.groupby(by=[custom_key])['dataDiff'].agg(
    [
        ('RecencyAgg', 'min')
    ]
)

# 计算F值 (消费次数)
F_agg = dataAll.groupby([custom_key])[custom_key].agg(
    [
        ('FrequencyAgg', np.size)
    ]
)

# 计算M值 (交易金额总数)
M_agg = dataAll.groupby([custom_key])['买家实际支付金额'].agg(
    [
        ('MonetaryAgg', np.sum)
    ]
)

# 将RFM的各个值连起来
aggData = R_agg.join(F_agg).join(M_agg)

# 计算R的等级分布
bins = aggData.RecencyAgg.quantile(
    q=[0, 0.25, 0.5, 1],
    interpolation='nearest'
)
bins[0] = 0
labels = [1, 2, 3]
R_S = pd.cut(
    aggData.RecencyAgg,
    bins, labels=labels
)

# 计算F的等级分布
bins = aggData.FrequencyAgg.quantile(
    q=[0, 0.5, 1],
    interpolation='nearest',
)
bins[0] = 0
labels = [2, 1]
F_S = pd.cut(
    aggData.FrequencyAgg,
    bins, labels=labels
)

# 计算M的等级分布
bins = aggData.MonetaryAgg.quantile(
    q=[0, 0.25, 0.5, 1],
    interpolation='nearest',
)
bins[0] = 0
labels = [3, 2, 1]
M_S = pd.cut(
    aggData.MonetaryAgg,
    bins, labels=labels
)

aggData['R_S'] = R_S
aggData['F_S'] = F_S
aggData['M_S'] = M_S

aggData['RFM'] = 100*R_S.astype(int) + 10*F_S.astype(int) + 1*M_S.astype(int)

# 将数据导入到RFM.csv文件中
aggData.to_csv('RFM.csv', encoding='utf-8')

print(aggData)

