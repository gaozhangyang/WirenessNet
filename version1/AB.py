import json
if __name__ =='__main__':
    ab=[(i,j) for i in range(2,101,1) for j in range(2,101,1)]
    print(len(ab))
    f=open('./AB.json','w')
    json.dump(ab,f)
    f.close()