import numpy as np
from numba import jit

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


def initAB(Ha, Wa, Hb, Wb):
    A = np.matrix(np.zeros((Ha, Wa), dtype=int), dtype=int)
    B = np.matrix(np.zeros((Hb, Wb), dtype=int), dtype=int)

    rowA = [i for i in range(0, Ha)]
    colA = [0 for i in range(0, Wa)]
    rowB = [i for i in range(0, Hb)]
    colB = [i for i in range(0, Wb)]

    A[rowA, colA] = 1
    B[rowB, colB] = 1

    return A, B


# @jit
def compare2(A, B):
    '''
    功能：
        比较A与B的激活矩阵，返回所有偏置下的通讯状况
    参数：
        A:节点A的激活矩阵
        B:节点B的激活矩阵
    返回：
        result: 当前情况下，节点A与B在不同偏置下的通讯状况
                每一行：(A的宽,B的宽,B的偏置,最小延迟)
    最大比较次数:偏置数*模板激活节点数=min(Wa^2,Wb^2)*length/max(Wa,Wb)
                适用于B节点矩阵比较小的情况
    '''
    Wa = A.shape[1]
    Ha = A.shape[0]
    Wb = B.shape[1]
    Hb = B.shape[0]
    num1 = A.shape[0]*A.shape[1]
    num2 = B.shape[0]*B.shape[1]
    # series1_: A节点矩阵拉伸成的行向量，长为num1
    series1_ = np.array(A).reshape(num1)
    # series2_：B节点矩阵拉伸成的行向量，长为num2
    series2_ = np.array(B).reshape(num2)
    lengh = lcm(num1, num2)

    delay=[]

    if num1 > num2:
        # 偏置加给B;以A为模板
        # result = np.zeros((num2, 5))
        for biasB in range(num2):
            # result[biasB, :] = Wa, Wb, 0, biasB, np.inf  # 默认找不到通讯点

            # series1 = np.tile(series1_, int(lengh/num1))
            # series2 = np.tile(series2_, int(lengh/num2))
            # series2 = np.roll(series2, biasB)
            # r = np.logical_and(series1, series2)
            # r2 = np.where(r == True)
            # if r2[0].shape[0] == 0:
            #     pass
            # else:
            #     result[biasB, :] = Wa, Wb, 0, biasB, r2[0][0]

            selectA = [i*Wa for i in range(0, int(lengh/Wa))]
            series2 = np.roll(series2_, biasB)
            delay.append(np.inf)
            for n in selectA:  # 循环寻找通讯点
                if series2[n % num2] == 1:
                    # result[biasB, :] = Wa, Wb, 0, biasB, n
                    delay[-1]=n
                    break
        return np.array([Wa,Wb,round(sum(delay)/len(delay),2),max(delay)])
    else:
        # 偏置加给A;以B为匹配模板
        # result = np.zeros((num1, 5))
        for biasA in range(num1):
            # result[biasA, :] = Wa, Wb, biasA, 0, np.inf  # 默认找不到通讯点

            # series1 = np.tile(series1_, int(lengh/num1))
            # series2 = np.tile(series2_, int(lengh/num2))
            # series1 = np.roll(series1, biasA)
            # r = np.logical_and(series1, series2)
            # r2 = np.where(r == True)
            # if r2[0].shape[0] == 0:
            #     pass
            # else:
            #     result[biasA, :] = Wa, Wb, biasA,0, r2[0][0]

            series1 = np.roll(series1_, biasA)
            selectB = [i*(Wb+1)-i//Hb*Wb for i in range(0, int(lengh/Wb))]
            delay.append(np.inf)
            for n in selectB:  # 循环寻找通讯点
                if series1[n % num1] == 1:
                    # result[biasA, :] = Wa, Wb, biasA, 0, n
                    delay[-1]=n
                    break
        return np.array([Wa,Wb,round(sum(delay)/len(delay),2),max(delay)])
