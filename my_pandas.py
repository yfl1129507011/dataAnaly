# -*- encoding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd

# 要使用pandas，首先要熟悉它的两个主要数据结构：Series和DataFrame
# Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）
# 以及与之相关的数据标签（即索引）组成

obj = Series([4, 7, -5, 3])

print(obj)

