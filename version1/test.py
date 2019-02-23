from node import compare2,initAB
import pandas as pd
import numpy as np
import json
import time

#测试流程
f=open('./AB.json','r');ab=json.load(f);f.close()

one=ab[0]
A,B=initAB(9,9,3,3)
result=compare2(A,B)
print(result)

R=pd.DataFrame(result,columns=['A','B','avg_Delay','max_Delay'])
R.to_csv('./result.csv')


# #测试roll速度
# t1=time.time()
# a=np.arange(400)
# for i in range(0,1000):
#     np.roll(a,i)
# t2=time.time()
# print(t2-t1)


# #测试与运算速度
# a=np.zeros((1,10000))
# b=np.ones_like(a)
# t1=time.time()
# for i in range(1000):
#     c=np.logical_and(a,b)
# t2=time.time()
# print(np.where(c==True))
# print(t2-t1)