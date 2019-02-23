
def is_prime(n):
	for i in range(2,int(n**0.5)):
		if n%i==0:
			return False
	return True

if __name__ == '__main__':
	num=0
	for i in range(2,10001):
		if is_prime(i):
			num+=1
	print(num)