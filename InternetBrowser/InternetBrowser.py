n=int(raw_input())
vow=['a','e','i','o','u']
for i in xrange(0,n):
	ip=raw_input()
	n1=len(ip)
	ip=ip[4:-4]
	count=0
	for ele in ip:
		if ele not in vow:
			count+=1
	print str(count+4)+"/"+str(n1)