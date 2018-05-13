# -*- encoding: utf-8 -*-

import pandas as pd
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
sku.index = jobList

# 画图操作
# for i, val in enumerate(sku.values.tolist()):   # 给每个柱子设置值
#     pl.text(i, val, '%.1f' % val, ha='center', va='bottom', fontsize=15)
pl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
pl.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号
pl.xlabel("工作职责")  # 设置x轴标记
pl.ylabel("SKU数量")  # 设置y轴标记
pl.title("SKU和工作职责的关系")   # 设置图的标题
sku.plot(kind='bar')
pl.show()
