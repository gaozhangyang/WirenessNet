import numpy as np
import pandas as pd
from numba import jit
from node2 import my_compare
import time
import json
import argparse
from addab import getAdd


def LetsGO(s,e,name):
	f=open('./AB.json','r');ab=json.load(f);f.close()

	one=ab[s];s+=1
	result=my_compare(one[0],one[1])
	t1=time.time()
	while 1:
		one=ab[s];s+=1
		tmp=my_compare(one[0],one[1])
		try:
			result=np.vstack((result,tmp))
		except:
			emm=1
		if s%100==0:
			print(s)
		if s==e+1:
			break
	R=pd.DataFrame(result,columns=['A','B','max_Delay'])
	R.to_csv('./result_{}.csv'.format(name))

	t2=time.time()
	print(t2-t1)

def add_Go(s,e,name):
	f = open('./AB.json', 'r');ab = json.load(f);f.close()
	one = ab[s];
	s += 1
	add = getAdd(one[0], one[1])
	t1 = time.time()
	while 1:
		one = ab[s];
		s += 1
		tmp = getAdd(one[0], one[1])
		try:
			result = np.vstack((add, tmp))
		except:
			emm = 1
		if s % 100 == 0:
			print(s)
		if s == e + 1:
			break
	R = pd.DataFrame(result, columns=['A','B','add'])
	R.to_csv('./add_{}.csv'.format(name))

	t2 = time.time()
	print(t2 - t1)

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('-s','--param_start',help='start of residue')
	parser.add_argument('-e','--param_end',help='end of residue')
	parser.add_argument('-name','--param_name',help='name of result')
	ARGS=parser.parse_args()
	s=int(ARGS.param_start)
	e=int(ARGS.param_end)
	name=str(ARGS.param_name)
	# s=9798;e=9800;name='0-100'
	LetsGO(s,e,name)
	# add_Go(s,e,name)