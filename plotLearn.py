# python绘图和可视化

import numpy as np
import pylab as pl

x = np.random.uniform(1, 100, 1000)
y = np.log(x) + np.random.normal(0, .3, 1000)

pl.scatter(x, y, s=1, label="log(x) with noise")

pl.plot(np.arange(1, 100), np.log(np.arange(1, 100)), c="b", label="log(x) true function")
pl.xlabel("x")
pl.ylabel("f(x) = log(x)")
pl.legend(loc="best")
pl.title("A Basic Log Function")
pl.show()

exit()
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import pylab as pl
# import matplotlib.pyplot as pl

# fig = pl.figure()  # 创建Figure对象
# ax1 = fig.add_subplot(2, 2, 1)  # 创建子画板
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
#
# pl.plot(np.arange(10))
# pl.show()

# data = Series(np.random.randn(1000).cumsum(), index=np.arange(1000))
# data.plot()
# pl.show()

df = DataFrame(
    np.random.rand(6, 4),
    index=['one', 'two', 'three', 'four', 'five', 'six'],
    columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus')
)
# df.plot(kind='line')  # 折线图
# df.plot(kind='bar')  # 柱状图
# df.plot(kind='barh')  # 条形图
df.plot(kind='kde')  # 密度图
pl.show()
