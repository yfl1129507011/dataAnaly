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

#fiveData = data.head()   # 获取前五行数据

# 计算R值(每个客户距离现在最近的天数)
R_agg = data.groupby(by=['mobile'])['dataDiff'].agg(
    [
        ('RecencyAgg', 'min')
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

# 计算R的阀值系数  大于R平均数为0，否则是1
aggData.RecencyAgg = np.where(aggData.RecencyAgg > np.average(aggData.RecencyAgg), 0, 1)

# 计算F的阀值系数  大于F平均数为1，否则是0
aggData.FrequencyAgg = np.where(aggData.FrequencyAgg > np.average(aggData.FrequencyAgg), 1, 0)

# 计算M的阀值系数  大于F平均数为1，否则是0
aggData.MonetaryAgg = np.where(aggData.MonetaryAgg > np.average(aggData.MonetaryAgg), 1, 0)

RFM = aggData.groupby(['RecencyAgg', 'FrequencyAgg', 'MonetaryAgg']).size()
print(aggData)

# RecencyAgg  FrequencyAgg  MonetaryAgg
# 0           0             0                37
# 0           0             1              3240
# 0           1             0                 2
# 0           1             1               222
# 1           0             0              2037
# 1           0             1              2025
# 1           1             0               380
# 1           1             1               463
