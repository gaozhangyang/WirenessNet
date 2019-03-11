import pandas as pd 
from scipy import io
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-csv', '--param_csv', help='name of csv')
	parser.add_argument('-mat', '--param_mat', help='name of mat')
	ARGS = parser.parse_args()

	name_csv = str(ARGS.param_csv)
	name_mat = str(ARGS.param_mat)

	dfdata=pd.read_csv('./{}.csv'.format(name_csv))
	data=dfdata.values
	io.savemat('./{}.mat'.format(name_mat),{'r':data[:,1:4]})