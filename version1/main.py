import numpy as np
from numba import jit
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
def Go():
	delay=[]
	for duty in range(10,100,10):
		for k in range(-3,6):
			b=duty+k
			a=b-2
			if gcd(a,b**2)<=b:
				A=Node(a,a)
				B=Node(b,b)
				s1=[(i, 0) for i in range(0, a)]
				s2=[(i, i) for i in range(0, b )]
				A.set(s1)
				B.set(s2)
				for d in range(0, a**2):
					re,A_,B_ = A.compare(A, B, d)
					all = np.sum(re)
					if all == 0:
						print("False! a:{},b:{},d:{}".format(a, b, d))
					else:
						delay.append(np.where(re==1)[0][0])
		print('duty:{},avg:{},max:{}'.format(duty,sum(delay)/len(delay),max(delay)))
		delay=[]

def save(info,err,invalid):
	t=int(time.time())
	f=open('./Ginfo_{}.json'.format(t),'w+')
	json.dump(info,f)
	f.close()

	f=open('./Gerr_{}.json'.format(t),'w+')
	json.dump(err,f)
	f.close()

	f=open('./Ginvalid_{}.json'.format(t),'w+')
	json.dump(invalid,f)
	f.close()


def read():
	f=open('./info.json','r+',encoding='utf-8')
	info=json.load(f)
	f.close()

	f=open('./err.json','r+',encoding='utf-8')
	err=json.load(f)
	f.close()

	f=open('./handled.json','r+',encoding='utf-8')
	handled=json.load(f)
	handled=[tuple(one) for one in handled]
	f.close()

	f=open('./residue.json','r+',encoding='utf-8')
	residue=json.load(f)
	residue=[tuple(one) for one in residue]
	f.close()

	return info,err,handled,residue

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('-s','--param_start',help='start of residue')
	parser.add_argument('-e','--param_end',help='end of residue')
	ARGS=parser.parse_args()
	s=int(ARGS.param_start)
	e=int(ARGS.param_end)

	t0=time.time()
	f=open('./residue.json','r')
	ab=json.load(f)
	f.close()

	info=[];err=[];invalid=[]
	delay=[]

	while 1:
		one=ab[s]
		a=one[0];b=one[1];
		t1 = time.time()
		if gcd(a,b**2)>b:
			invalid.append((a,b))
		else:
			A=Node(a,a)
			B=Node(b,b)
			s1=[(i, 0) for i in range(0, a)]
			s2=[(i, i) for i in range(0, b)]
			A.set(s1)
			B.set(s2)
			bb=b**2

			W=A.mat.shape[1]
			H=A.mat.shape[0]
			num1=A.mat.shape[0]*A.mat.shape[1]
			num2=B.mat.shape[0]*B.mat.shape[1]
			series1 = np.array(A.mat).reshape(num1)
			series2_ = np.array(B.mat).reshape(num2)
			lengh=lcm(num1,num2)

			for d in range(0,bb):
				series2=np.roll(series2_,d)
				# print('{}/{}'.format(d,bb))
				# print('d:',d)
				# print('s1:',series1)
				# print('s2:',series2)
				re= A.compare2(series1,series2,num1,num2,lengh,H,W)
				if re == -1:
					errtmp={'a':a,'b':b,'d':d}
					err.append(errtmp)
					print(errtmp)
				else:
					delay.append(re)
				# print(delay)
			t2 = time.time()
			print('{}/{} a:{},b:{},time:{}'.format(s,e,a,b,t2 - t1))
			info.append({'a':a,'b':b,'duty_a':1/a,'duty_b':1/b,'avg':sum(delay)/len(delay),'max':max(delay)})
			print(info[-1])
			print()
			delay=[]
		s+=1
		if s==e:
			break

	t3=time.time()
	print('all time: {}'.format(t3-t0))
	print('info:',info)
	print('err:',err)
	save(info,err,invalid)
	