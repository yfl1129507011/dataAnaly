import pandas
import numpy as np
from pandas import DataFrame

df = DataFrame(
    {
        'key1': ['a', 'a', 'b', 'b', 'a'],
        'key2': ['one', 'two', 'one', 'two', 'one'],
        'key3': [1, 2, 3, 4, 5],
        'data1': np.random.randn(5),
        'data2': np.random.randn(5),
        'data3': [54, 49, 28, 26, 0]
    }
)

mean_all = df.groupby(df['key1']).mean()
mean_one = df.groupby('key1')['data3'].mean()
# '无索引'形式返回聚合数据
mean_one1 = df.groupby('key1', as_index=False)['data3'].mean()

size = df.groupby(df['key2']).size()

agg1 = df.groupby('key2')['data3'].agg('std')  # 标准差
agg2 = df.groupby(['key2'])['data3'].agg(
    [
        ('ageMin', 'min'),
        ('ageMax', np.max),
        ('aggSum', 'sum'),
        ('aggMedian', np.median),  # 算术中位数
        ('aggVar', 'var')  # 方差
    ]
)

print(mean_one1)