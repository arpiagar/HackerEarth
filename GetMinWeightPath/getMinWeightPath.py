name = raw_input().split(' ')
n,k1,k2,k3,k4 = [int(x) for x in name]
MOD = 1000000007
def fib(n):
	fib0=0
	fib1=1
	val=0
	for i in xrange(1,n):
		temp=fib1
		fib1=fib0+fib1
		fib0=temp
	return fib1
	
class Node:
	def __init__(self,nid):
		self.id=nid;
		self.nodemap={};

class Graph:
	def __init__(self,n,k1,k2,k3,k4):
		self.numnodes=0
		self.nodesmap={}
		for i in xrange(0,n):
			for j in xrange(0,n):
				self.addNode(Node((i,j)))
		count=0
		for i in xrange(0,n):
			for j in xrange(0,n-1):
				self.linkNodes(self.nodesmap[(i,j)],self.nodesmap[(i,j+1)],fib(k1+count)+fib(k2+count))
				count+=1
		count=0
		for i in xrange(0,n):
			for j in xrange(0,n-1):
				self.linkNodes(self.nodesmap[(j,i)],self.nodesmap[(j+1,i)],fib(k3+count)+fib(k4+count))
				count+=1
		
			
	def addNode(self,nodeobj):
		self.numnodes+=1
		self.nodesmap[nodeobj.id]=nodeobj
		
	def linkNodes(self,node1,node2,weight):
		if not self.nodesmap.has_key(node1.id) or not self.nodesmap.has_key(node2.id):
			raise "Register nodes first"
		else:
			node1.nodemap[node2.id]=weight
			node2.nodemap[node1.id]=weight
	
	def getminPath(self,node,summ):
		x,y=node.id
		w1=None
		w2=None
		if x+1<n:
			w1=self.nodesmap[(x,y)].nodemap[(x+1,y)]
		if y+1<n: 
			w2=self.nodesmap[(x,y)].nodemap[(x,y+1)]
		if w1!=None and w2!=None:
			if w1>w2:
				return self.getminPath(self.nodesmap[(x,y+1)],summ+w2)
			else:
				return self.getminPath(self.nodesmap[(x+1,y)],summ+w1)
		if w1==None and w2!=None:
			return self.getminPath(self.nodesmap[(x,y+1)],summ+w2)
		elif w1!=None and w2==None:
			return self.getminPath(self.nodesmap[(x+1,y)],summ+w1)
		else:
			return summ
	

		
G=Graph(n,k1,k2,k3,k4)
print G.getminPath(G.nodesmap[(0,0)],0)
