import numpy as np
import pandas as pd
from numba import jit
from node import compare3,initAB
import time
import json
import argparse


# @jit
def LetsGO(s,e,name):
	f=open('./AB.json','r');ab=json.load(f);f.close()

	one=ab[s];s+=1
	A,B=initAB(one[0],one[0],one[1],one[1])
	result=compare3(A,B)
	t1=time.time()
	while 1:
		one=ab[s];s+=1
		A,B=initAB(one[0],one[0],one[1],one[1])
		tmp=compare3(A,B)
		result=np.vstack((result,tmp))
		if s%100==0:
			print(s)
		if s==e+1:
			break
	R=pd.DataFrame(result,columns=['A','B','max_Delay','bios'])
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
	
	