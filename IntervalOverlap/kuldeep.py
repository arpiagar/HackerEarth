num=int(raw_input())
temp=[]
for i in xrange(0,num):		
        l1=raw_input().split('-') 
       	t1=l1[0].split(":")
	t1=float(t1[0])+float(t1[1])/60
	t2=l1[1].split(":")
	t2=float(t2[0])+float(t2[1])/60
	temp.append([t1,t2])


sorted(temp,key=lambda temp:temp[1])
n=len(temp)
flag=0
import pdb;pdb.set_trace()
for i in xrange(0,n):
	val=temp[i][1]
	for j in xrange(i+1,n):
		if temp[j][0]<val:
			flag=1
	 		break
	if flag==1:
		break
if flag==1:
	print "Will need a moderator!"
else:
	print "Who needs a moderator?"
