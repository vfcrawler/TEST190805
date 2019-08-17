import numpy as np
import random

# 生成区间内的正整数
ret1 = random.randint(20,50)

# 生成5个标准正态分布随机小数
ret2 = np.random.randn(5)

# 生成0-1的随机小数
ret3 = np.random.rand(5)

# 生成0-1的随机小数
ret4 = random.random()

print('生成区间内的正整数:',ret1)
print('生成5个标准正态分布随机小数:',ret2)
print('生成0-1的随机数:',ret4)




