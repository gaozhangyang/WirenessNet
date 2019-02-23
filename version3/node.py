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


@jit
def initAB(Ha, Wa, Hb, Wb):
    A = np.matrix(np.zeros((Ha, Wa), dtype=int), dtype=int)
    B = np.matrix(np.zeros((Hb, Wb), dtype=int), dtype=int)

    rowA = [i for i in range(0, Ha)]
    colA = [0 for i in range(0, Wa)]
    rowB = [i for i in range(0, Hb)]
    colB = [i for i in range(0, Wb)]

    A[rowA, colA] = 1
    B[rowB, colB] = 1
    return A,B



def compare3(A,B):
    Wa = A.shape[1]
    Ha = A.shape[0]
    Wb = B.shape[1]
    Hb = B.shape[0]
    num1 = A.shape[0]*A.shape[1]
    num2 = B.shape[0]*B.shape[1]
    length=lcm(num1,num2)

    # series1_: A节点矩阵拉伸成的行向量，长为num1
    series1_ = np.array(A).reshape(num1)
    # series2_：B节点矩阵拉伸成的行向量，长为num2
    series2_ = np.array(B).reshape(num2)

    if num1>num2:
        #以A为模板，偏置给B
        allBias=set(range(0,num2))
        a_=np.where(series1_==1)[0]
        b=np.where(series2_==1)[0]
        a=[s+num1*i for i in range(int(length/num1)) for s in np.nditer(a_)]

        delay=[]
        for ai in a:
            #偏差，series2_中激活点相对于ai的位置偏差
            bias=set(np.where(np.roll(series2_,-ai)==1)[0])
            #减去合法偏差
            allBias=allBias-bias
            #由于A固定从A0开始，所有激活点ai所处时间就是延迟，第一次相互发现的时候
            delay += [(ai,one) for one in bias]
            if len(allBias)==0:
                index=np.argmax([th[0] for th in delay], axis=0)
                return np.array([Wa,Wb,delay[index][0],delay[index][1]])
        return np.array([Wa,Wb,np.inf,None])
            
    else:
        #以B为模板，偏置给A
        allBias=set(range(0,num1))
        a=np.where(series1_==1)[0]
        b_=np.where(series2_==1)[0]
        b = [s + num2 * i for i in range(int(length / num2)) for s in np.nditer(b_)]

        delay=[]
        for bi in b:
            #偏置
            bias=set(np.where(np.roll(series1_,-bi)==1)[0])
            #减去合法偏置
            allBias=allBias-bias
            delay += [(bi,one) for one in bias]
            if len(allBias)==0:
                index=np.argmax([th[0] for th in delay], axis=0)
                return np.array([Wa,Wb,delay[index][0],delay[index][1]])
        return np.array([Wa,Wb,np.inf,None])

