import pandas as pd 
from scipy import io

if __name__ == '__main__':
	dfdata=pd.read_csv('./result_all.csv')
	data=dfdata.values
	io.savemat('./all_results.mat',{'r':data[:,1:5]})