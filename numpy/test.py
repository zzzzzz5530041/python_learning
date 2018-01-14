import numpy as np;

arr = np.arange(15);##生成15个元素的一维数组 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]


arr = arr.reshape(3,5)## reshape 将arr一维数组转成3行5列的2维数组
print(arr.dtype)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''

a = np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3));
print(a)
