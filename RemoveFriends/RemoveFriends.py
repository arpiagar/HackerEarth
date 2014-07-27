n=int(raw_input())
for i in xrange(0,n):
	l1=raw_input().split(' ')
	n,dnum=int(l1[0]),int(l1[1])
	l1=raw_input().split(' ')
	l1=[int(x) for x in l1]
	while dnum!=0:
		n=len(l1)
		i=0
		while (i<n-1):
			if l1[i]<l1[i+1]:
				l1.remove(l1[i])
				dnum-=1
				break
			i=i+1
	p=[]

	while dnum>0:
		flag=False
		while i<len(l1)-1:
			if l1[i] <l1[i+1]:
				l1.remove(l1[i])
				dnum-=1
				flag=True
				break
			i+=1
		if not flag:
			l1.remove(l1[len(l1)-1])
			dnum-=1
		
			
#		for i in xrange(0,len(l1)):
#			if l1[i]<l1[i+1]:
#				p.append(l1[i])
#		if len(p)> dnum:
#			break
#		for ele in p:
			
	str1=""
	for ele in l1:
		str1+=str(ele)+" "
	print str1[:-1]
				
