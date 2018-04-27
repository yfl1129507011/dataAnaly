import numpy as np
import pandas

data = pandas.read_excel(
    'bbb.xlsx',
    [0, 1],  # 指定sheet表,可以指定多个sheet
    None,  # 指定列名称，0表示取第一行为列名, None表示列名为从0开始的索引数字
    [0],  # 忽略指定的行，0表示第一行
    0,  # 省略从尾部数的int行数据
    None,  # 指定索引列
    ['sale_date', 'product_name', 'name', 'mobile'],  # 自定义列名
    [0, 1, 2, 3]   # 选定所需的列
)
data = pandas.concat(data)  # 合并数据
print(data)
exit()
priceList = {
    '高达卫士': 4499,
    '高达P': 4499,
    'N280新风': 560,
    'M160S': 400,
    'M160': 360,
    'BR150': 5480,
    'N280': 8980,
}

data['price'] = data['product_name'].map(str.upper).map(priceList)  # 数据转换

# 计算交易时间距离现在的天数
data['dataDiff'] = pandas.to_datetime('today')-data['sale_date']
data['dataDiff'] = data['dataDiff'].dt.days
# 计算R值(每个客户距离现在最近的天数)
R_agg = data.groupby(by=['mobile'])['dataDiff'].agg(
    [
        ('RecencyAgg', np.min)
    ]
)

# 计算F值 (消费次数)
F_agg = data.groupby(['mobile'])['mobile'].agg(
    [
        ('FrequencyAgg', np.size)
    ]
)

# 计算M值 (交易金额总数)
M_agg = data.groupby(['mobile'])['price'].agg(
    [
        ('MonetaryAgg', np.sum)
    ]
)

# 将RFM的各个值连起来
aggData = R_agg.join(F_agg).join(M_agg)

# 计算R的阀值系数
bins = aggData.RecencyAgg.quantile(
    q=[0, 0.2, 0.4, 0.6, 0.8, 1],
    interpolation='nearest'
)
labels = [5, 4, 3, 2, 1]
R_S = pandas.cut(
    aggData.RecencyAgg,
    bins, labels=labels
)

# 计算F的阀值系数
bins = aggData.MonetaryAgg.quantile(
    q=[0, 0.2, 0.4, 0.6, 0.8, 1],
    interpolation='nearest'
)
labels = [1, 2, 3, 4, 5]
F_S = pandas.cut(
    aggData.FrequencyAgg,
    bins, labels=labels
)
