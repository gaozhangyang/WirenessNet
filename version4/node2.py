import numpy as np
from numba import jit
import copy


# 定义函数
@jit
def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


@jit
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


# @jit
def compare4(raw_a,raw_b,T1, active_A, T2, active_B):
    rawT1, rawT2, = T1, T2
    if T1 <= T2:
        T1, T2 = T2, T1
        active_A, active_B = active_B, active_A
    active_A, active_B = np.array(active_A), np.array(active_B)
    LA, LB = len(active_A), len(active_B)
    b = np.repeat(active_B, LA)
    a = np.tile(active_A, LB)
    ba = (b - a)
    delay = []
    Set2 = set(range(0, T2))
    for mx in range(0, T2):
        tmp = ba % T2#将完全剩余系转化到>=0的情况
        tmps = set(tmp)
        tmpSet2 = copy.deepcopy(Set2)
        Set2 -= tmps
        if len(Set2) == 0:
            cross = tmpSet2 & tmps
            for one in cross:
                index = np.where(tmp == one)
                # 每一个delta下求最小的发现延迟
                a_ = min(a[index])
                delay.append(mx * T1 + a_)
            # 不同delta之间取最大的发现延迟
            delay = max(delay)
            return np.array([raw_a, raw_b, delay])
    return np.array([raw_a, raw_b, np.inf])


# @jit
def my_compare(a, b):

    # #my/quorum
    # T1 = a * a
    # T2 = b * b
    # A = [k*a  for k in range(0, a)]+[k  for k in range(0, a)]
    # B = [k * b for k in range(0, b)]+[k  for k in range(0, b)]

    # #U-Connect/hello
    # T1 = a * a
    # T2 = b * b
    # A = [k * a  for k in range(0, a)]+[k  for k in range(0, int(np.ceil(a/2)))]
    # B = [k * b for k in range(0, b)]+[k  for k in range(0, int(np.ceil(b/2)))]

    # # Hedis
    # T1 = a * (a + 1)
    # T2 = b * (b + 1)
    # A = [k * (a+1) for k in range(0, a)] + [k*(a+2)+1 for k in range(0, a)]
    # B = [k * (b+1) for k in range(0, b)] + [k*(b+2)+1 for k in range(0, b)]
    # delay = compare4(T1, A, T2, B)

    # Searchlight
    # T1 = a * 2*a
    # T2 = b * 2*b
    # A = [k * (2*a) for k in range(0, a)] + [k * (2*a)+k + 1 for k in range(0, a)]
    # B = [k * (2*b) for k in range(0, b)] + [k * (2*b)+k + 1 for k in range(0, b)]



    delay = compare4(a,b,T1, A, T2, B)
    return delay


if __name__ == '__main__':
    # 假设a>b，小的那个一列，大的那个连续b个
    a=3
    b=4
    T1 = a * 2 * a
    T2 = b * 2 * b
    A = [k * (2 * a) for k in range(0, a)] + [k * (2 * a) + k + 1 for k in range(0, a)]
    B = [k * (2 * b) for k in range(0, b)] + [k * (2 * b) + k + 1 for k in range(0, b)]

    delay = compare4(a,b,T1, A, T2, B)
    print('a:{} b:{} delay:{}'.format(a, b, delay))
