# -*- encoding:utf-8 -*-

# NumPy(Numerical Python的简称) 是高性能科学计算机和数据分析的基础包。部分功能如下：
# 1. ndarray(N维数组对象), 一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组
# 2. 用于对数组数据进行快速运算的标准数学函数（无需编写循环）
# 3. 用于读写磁盘数据的工具以及用户操作内存映射文件的工具
# 4. 线性代数、随机数生成以及傅里叶变换功能
# 5. 用于集成由C、C++、Fortran等语言编写的代码工具

import numpy as np

# 创建ndarray
data1 = [1, 2, 3, 4, 5.5]
arr1 = np.array(data1)  # [ 1.   2.   3.   4.   5.5]
dtype1 = arr1.dtype  # 查看数据类型float64
ndim1 = arr1.ndim  # 查看维度  1
shape1 = arr1.shape  # (5,)
size1 = arr1.size  # 5

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
dtype2 = arr2.dtype  # int32
ndim2 = arr2.ndim  # 2
shape2 = arr2.shape  # (2, 4)
size2 = arr2.size  # 数组元素的数目
float_arr2 = arr2.astype(np.float64)  # 转换类型
dtype2 = float_arr2.dtype  # float64

arr = arr2 * np.array([11, 22, 33, 44])

arr22 = np.where(arr > 55, 1, 0)
print(arr22)
