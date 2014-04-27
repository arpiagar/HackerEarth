

num = int(raw_input())

class Node:
	def __init__(self,val,senior):
		self.val=val
		self.juniors=[]
		self.senior=senior

class Tree:
	def __init__(self,n):
		self.length=n
		self.commander=-1


def communicate(tree_map,commander,sender,receiver):
	temp=tree_map[sender]
	count=0
	flag=0
	while temp.senior!=0:
		if temp.senior==receiver:
			print count
			flag=1
			break
		temp=tree_map[temp.senior]
		count +=1
	if  flag==0:
		print -1



def createTree(arr):
	temp=[]
	tree_map={}
	commander=-1
	temp.append(-2)
	for x in arr:#Adding a dummy value -2 at 0th index of temp and then pushing all the other elements
		temp.append(x)
	for i in xrange(1,len(temp)):
		tree_map[i]=Node(i,temp[i])
		if temp[i]==0:
			commander=i
	print tree_map
	
	for  k,v in tree_map.iteritems():
		senior=v.senior
		if senior!=0:
			tree_map[senior].juniors.append(k)
	
	return commander,tree_map

for i in xrange(0,num):
	n= int(raw_input())
	tree=raw_input().split(' ')
	tree=[int(x) for x in  tree]
	message_num=int(raw_input())
	message_list=[]
	for j in xrange(0,message_num):
		v1,v2=raw_input().split(' ')
		v1,v2=int(v1),int(v2)
		message_list.append((v1,v2))
	
	commander,tree_map=createTree(tree)
	import pdb;pdb.set_trace()
	for j in xrange(0,message_num):
		sender,receiver=message_list[j][0],message_list[j][1]
		communicate(tree_map,commander,sender,receiver)
	


