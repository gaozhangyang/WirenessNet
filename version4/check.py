import numpy as np

def initAB(Ha, Wa, Hb, Wb):
    A = np.matrix(np.zeros((Ha, Wa), dtype=int), dtype=int)
    B = np.matrix(np.zeros((Hb, Wb), dtype=int), dtype=int)

    rowA = [i for i in range(0, Ha)]+[0 for i in range(0, Wa)]
    colA = [0 for i in range(0, Ha)]+[i for i in range(0, Wa)]
    rowB = [i for i in range(0, Hb)]+[0 for i in range(0, Wb)]
    colB = [0 for i in range(0, Hb)]+[i for i in range(0, Wb)]

    A[rowA, colA] = 1
    B[rowB, colB] = 1

    num1 = A.shape[0] * A.shape[1]
    num2 = B.shape[0] * B.shape[1]
    # series1_: A节点矩阵拉伸成的行向量，长为num1
    series1_ = np.array(A).reshape(num1)
    # series2_：B节点矩阵拉伸成的行向量，长为num2
    series2_ = np.array(B).reshape(num2)

    return series1_,series2_

def check(listA,listB):
    if len(listA)<=len(listB):
        listA,listB=listB,listA
    T1,T2=len(listA),len(listB)
    delay=[]
    for delta in range(0,T2):
        listB_=np.roll(listB,-delta)
        for i in range(0,T1*T2):
            if listA[i%T1]+listB_[i%T2]==2:
                delay.append(i)
                break
    return max(delay)

if __name__ == '__main__':
    a=38
    b=54
    A,B=initAB(a,a,b,b)
    delay=check(A,B)
    print(delay)
