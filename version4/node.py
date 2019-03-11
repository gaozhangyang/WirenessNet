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
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a,b = b,a%b
    return a

@jit
def GetXY(A,B):
    '''
        计算AX+BY=1中的Y、X
    '''
    d=gcd(A,B)
    if A>=B:
        if A%B==0:
            k=A/B
            return np.array([1/B,(1-k)/B])
        reverse=False
        
    if A<B:
        if B%A==0:
            k=B/A
            return np.array([(1-k)/A,1/A])
        reverse=True
        tmp=A;A=B;B=tmp
    
    r=0;Q=[]
    while r!=1:
        q=A//B; r=A%B
        Q.append(q)
        A=B;    B=r
    Q.reverse()
    H=len(Q)
    Hs=np.array(range(0,H))
    mat=np.matrix(np.zeros((H,H+2)))
    mat[Hs,Hs]=1
    mat[Hs,Hs+1]=Q
    mat[Hs,Hs+2]=-1
    for i in range(1,H):
        mat[0,:]-=mat[i,:]*mat[0,i]

    if reverse:
        return np.array([-mat[0,-2],-mat[0,-1]])
    else:
        return np.array([-mat[0,-1],-mat[0,-2]])
@jit
def Solve(A,B,C):
    d=gcd(A,B)
    if C%d !=0:
        return False
    else:
        A/=d;B/=d;C/=d
        XY=GetXY(A,B)
        XY=XY*C
        k=np.floor(XY[0]/B)#使得A最小但大于0
        return np.array([XY[0]-k*B,XY[1]+k*A])



def compare4(T1,active_A,T2,active_B):
    raw_T10, raw_T20 = T1, T2

    if T1<T2:
        T1,T2=T2,T1
        active_A,active_B=active_B,active_A
    active_A ,active_B= np.array(active_A),np.array(active_B)

    raw_T1, raw_T2 = T1, T2
    d = gcd(T1, T2)
    T1, T2 = int(T1 / d), int(T2 / d)

    #求m撇
    mn_ = GetXY(T1, T2)
    mn_[1] = -mn_[1]
    # print('mn撇: {}'.format(mn_))

    #求m0
    LA,LB,LDelta=len(active_A),len(active_B),raw_T2
    b_ = np.repeat(active_B, LA*LDelta)
    a_ = np.tile(np.repeat(active_A,LDelta),LB)
    delta = np.tile(np.arange(0, LDelta), LA*LB)
    ab_delta = (b_-a_ - delta)
    m0 = ab_delta/d * mn_[0]

    #T1,T2可约时，有可能无解，把无解的情况标记出来
    invalid=m0%1!=0

    #求m星
    kx = np.floor((m0 + a_ / raw_T1) / T2)
    mx=m0-kx*T2
    mx[invalid]=np.inf
    # valid = mx >= 0

    #求delay
    delay = mx * raw_T1 + a_
    # delay = delay[valid]
    # delay[delay % 1 != 0] = 0
    delay2=np.reshape(delay,(int(len(delay)/LDelta),LDelta))
    minDelay=np.max(np.min(delay2,0))
    # print('m星: {}'.format(mx))
    # print('a_:{}'.format(a_))
    # print('delay:{}'.format(delay))
    return np.array([np.sqrt(raw_T10),np.sqrt(raw_T20),minDelay])



def my_compare(a,b):
    T1 = a * a;
    T2 = b * b
    A = [k * a for k in range(0, a)];
    B = [k * (a + 1) for k in range(0, a)]
    delay = compare4(T1, A, T2, B)
    return delay


if __name__ == '__main__':
    a=2;b=4
    T1=a*a;T2=b*b
    # re=Solve(T1,T2,3)
    # print(re)
    A=[k*a for k in range(0,a)];B=[k*(b+1) for k in range(0,b)]
    delay=compare4(T1,A,T2,B)
    print('T1:{}; T2:{}; delay: {}\n'.format(T1,T2,delay))