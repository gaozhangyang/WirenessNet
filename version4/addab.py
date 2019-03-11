import numpy as np

def getset(T1, active_A, T2, active_B):
    rawT1,rawT2,=T1,T2
    if T1<=T2:
        T1,T2=T2,T1
        active_A,active_B=active_B,active_A
    active_A, active_B = np.array(active_A), np.array(active_B)
    LA, LB = len(active_A), len(active_B)
    b = np.repeat(active_B, LA)
    a = np.tile(active_A, LB)
    ba=(b-a)

    Set2 = set(range(0, T2))
    tmps = set(ba%T2)
    return Set2-tmps,tmps

def my_getset(a,b):
    T1 = a * a
    T2 = b * b
    A = [k * a for k in range(0, a)]
    B = [k * (b + 1) for k in range(0, b)]
    re,tmps = getset(T1, A, T2, B)
    return re,tmps

def getAdd(a,b):
    re, tmps = my_getset(a,b)
    tmps = list(sorted(tmps))
    for i in range(0, len(tmps)-1):
        if tmps[i + 1] - tmps[i] != 1:
            return np.array([a,b,int(tmps[i + 1]/2)])

if __name__  == '__main__':
    add=getAdd(100,99)
    print(add)