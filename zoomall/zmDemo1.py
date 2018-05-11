# -*- encoding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

data = pd.read_excel(
    '美妆产品经理需求频度调研数据.xls',
    names=['cid', 'job', 'sku',
           '3_1', '3_2', '3_3', '3_4', '3_5', '3_6'
           ],
    parse_cols=[5, 6, 7, 8, 9, 10, 11, 12, 13]
)

# parse_cols = list(np.arange(5, 14))

sku = data.sku.groupby(data['job']).mean()
jobList = [
    '品牌经理',
    '产品开发及设计',
    '产品运营',
    '供应链对接',
    '以上全部',
    # '其他',
]
pl.rcParams['font.sans-serif'] = ['SimHei']
sku.index = jobList
pl.xlabel("工作职责")
pl.ylabel("SKU数量")
# pl.legend(loc="best")
pl.title("SKU和工作职责的关系")
sku.plot(kind='bar')
pl.show()
print(sku.name)
