import numpy as np
import pandas as pd
from numba import jit
from node import compare2,initAB
import time
import json
import argparse

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
def LetsGO(s,e,name):
	f=open('./AB.json','r');ab=json.load(f);f.close()

	one=ab[s];s+=1
	A,B=initAB(one[0],one[0],one[1],one[1])
	result=compare2(A,B)
	t1=time.time()
	while 1:
		one=ab[s];s+=1
		A,B=initAB(one[0],one[0],one[1],one[1])
		tmp=compare2(A,B)
		result=np.vstack((result,tmp))
		if s==e:
			break
		if s%100==0:
			print(s)
	R=pd.DataFrame(result,columns=['A','B','avg_Delay','max_Delay'])
	R.to_csv('./result_{}.csv'.format(name))

	t2=time.time()
	print(t2-t1)

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('-s','--param_start',help='start of residue')
	parser.add_argument('-e','--param_end',help='end of residue')
	parser.add_argument('-name','--param_name',help='name of result')
	ARGS=parser.parse_args()
	s=int(ARGS.param_start)
	e=int(ARGS.param_end)
	name=str(ARGS.param_name)

	LetsGO(s,e,name)
	
	