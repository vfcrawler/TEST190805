#方法2.使用reduce函数求和
from functools import reduce

count = reduce(lambda x,y:x+y,[1,2,3,10248])
print(count)