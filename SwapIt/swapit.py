n=int(raw_input())
for i  in xrange(0,n):
	a1=raw_input().split(' ')
	a2=raw_input().split(' ')
	num,swaps=[int(x) for x in a1]
	a2=[int(x) for x in a2]
	count=0
	while True:
		minm=min(a2[count:])
		idx=[i for i,x in enumerate(a2) if x == minm][0]
		while idx-1!=0 and swaps>0:
			temp=a2[idx]
			a2[idx]=a2[idx-1]
			a2[idx-1]=temp
			idx-=1
		if swaps==0:
			print a2
			break
			
			
	