import matplotlib.pyplot as plt
from random import normalvariate, sample
import re
from timeit import timeit
from turtle import position
from numpy.linalg import inv, qr
import numpy as np

arr = np.random.randn(5, 4)
arr = np.array([
    [2.1695, -0.1149, 2.0037, 0.0296],
    [0.7953, 0.1181, -0.7485, 0.585],
    [0.1527, -1.5657, -0.5625, -0.0327],
    [-0.929, -0.4826, -0.0363, 1.0954],
    [0.9809, -0.5895, 1.5817, -0.5287]
])
# print(arr)
#print(arr.mean(), np.mean(arr), arr.sum())
# print(arr.mean(axis=1))  # 모든컬럼에서 평균
# [ 1.021975  0.187475 -0.50205  -0.088125  0.3611  ]
# print(arr.sum(axis=0))  # 로우에서의 합
# [ 3.1694 -2.6346  2.2381  1.1486]

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# print(arr.cumsum())  # 누산함수 [ 0  1  3  6 10 15 21 28]
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(arr.cumsum(axis=0))
# print(arr.cumprod(axis=1))
arr = np.random.randn(100)
#print((arr > 0).sum())
bools = np.array([False, False, True, False])
#print(bools.any(), bools.all())

arr = np.array([0.6295, -0.4938, 1.24, -0.1357, 1.43, -0.8469])
# print(arr)
arr.sort()
# print(arr)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# print(np.unique(names))
# print(sorted(set(names)))

arr = np.arange(10)
np.save('1', arr)
# print(np.load('1.npy'))

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
# print(x)
# print(y)
#print(x.dot(y), np.dot(x, y))
# print(y.dot(x))
#print(np.dot(x, np.ones(3)))
#print(x @ np.ones(3))
#print(np.dot(y, np.ones(2)))
X = np.random.randn(5, 5)
mat = X.T.dot(X)
# print(mat)
# print(inv(mat))
# print(mat.dot(inv(mat)))
q, r = qr(mat)
# print(r)
#
N = 1000000
# %timeit samples = [normalvariate(0,1) for _ in range(N)]
rng = np.random.RandomState(1234)
# print(rng.randn(10))


def walk():
    import random
    position = 0
    walk = [position]
    steps = 1000
    for i in range(steps):
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk.append(position)

    # print(walk)
    # return walk
    # plt.plot(walk[:100])
    # plt.show()


#walk = walk()

def _177():
    nsteps = 1000
    draws = np.random.randint(0, 2, size=nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    print(walk.min(), walk.max(), (np.abs(walk) >= 10).argmax())
# _177()


def _178():
    nwalks = 5000
    nsteps = 1000
    draws = np.random.randint(0, 2, size=(nwalks, nsteps))
    steps = np.where(draws > 0, 1, -1)
    walks = steps.cumsum(1)
    print(walks)


_178()
