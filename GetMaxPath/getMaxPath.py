n = int(raw_input())


def getMaxPath(arr,row,col,i,k):
	l=0;r=0
	if i+1<row:
		if arr[i+1][k]>arr[i][k]:
			l=1+getMaxPath(arr,row,col,i+1,k)
	if k+1<col:
		if arr[i][k+1]>arr[i][k]:
			r=1+getMaxPath(arr,row,col,i,k+1)
	if l>r:
		return l
	else:
		return r
			
for i in xrange(0,n):
	l1=raw_input().split(' ')
	row,col=int(l1[0]),int(l1[1])
	count=0
	mainlist=[]
	for j in xrange(0,row):
		temp=raw_input().split(' ')
		temp=[int(x) for x in temp]
		mainlist.append(temp)
	import pdb;pdb.set_trace()	
	print getMaxPath(mainlist,row,col,0,0)
