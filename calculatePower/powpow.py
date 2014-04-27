MAX_POW=1000000007

num = int(raw_input())

def calculate(l1,maximum):
	sum1=0
	length=len(l1)
	for i in xrange(0,length):
		for j in xrange(i,length):
			sum1=sum1+abs(l1[i]-l1[j])
			
	print ((sum1%MAX_POW)*(maximum%MAX_POW))%MAX_POW


for i in xrange(0,num):
	n=int(raw_input())
	elem=raw_input().split(' ')
	elem=[int(x) for x in elem]
	maximum=max(elem)
	calculate(elem,maximum)
