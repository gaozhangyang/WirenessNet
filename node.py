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
def compare(self,a,b,bias):
    self.bias=bias
    num1=a.mat.shape[0]*a.mat.shape[1]
    num2=b.mat.shape[0] * b.mat.shape[1]
    series1 = a.mat.reshape(1, num1)
    series2 = b.mat.reshape(1, num2)
    lengh=lcm(num1,num2)
    series2=np.roll(series2,bias)
    series1_=np.tile(series1,int(lengh/num1))
    series2_=np.tile(series2,int(lengh/num2))

    # for i in range(0,lengh):
    #     series1_[0,i]=series1[0,i%num1]
    #     series2_[0,i]=series2[0,(i-bias)%num2]
    result=((series1_+series2_)>=2)*1
    result_=np.zeros((int(np.ceil(lengh**0.5)),int(np.ceil(lengh**0.5))))
    lengh_ = result_.shape[0] * result_.shape[1]
    for i in range(0,lengh_):
        result_[i//result_.shape[0],i%result_.shape[0]]=result[0,i%lengh]
    return result_,series1_,series2_

# @jit
def compare2(self,series1,series2,num1,num2,lengh,H,W):
    for i in range(int(lengh/num1*H)):#一共i行
        n=i*W
        if series1[n%num1]+series2[n%num2]>=2:
            return n
    return -1
