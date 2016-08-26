class Node:
	def __init__(self,value):
		self.value = value
		self.next  = None

class LinkedList:
	def __init__(self, list= []):
		self.head =  None
		for elem in list:
			self.add(Node(elem))

	def add(self,node):
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = node

l1 = LinkedList([2,4,6,9,40])
l2 = LinkedList([1,3,5,7,88])

def merge_linked_list(l1,l2):
  l3 = LinkedList()
  temp1 =  l1.head
  temp2 =  l2.head
  while True:
    #import pdb;pdb.set_trace()
    if temp1 == None:
      while temp2.next != None:
    		l3.add(Node(temp2.value))
    		temp2 = temp2.next
      break
    if temp2 == None:
      while temp1.next != None:
    		l3.add(Node(temp1.value))
    		temp1 = temp1.next
      break
    if temp1.value <= temp2.value:
    	l3.add(Node(temp1.value))
    	temp1  = temp1.next
    else:
    	l3.add(Node(temp2.value))
    	temp2 = temp2.next
  return l3
  
l1 = LinkedList([2,4,6,9,40])
l2 = LinkedList([1,3,5,7,88])

l3 = merge_linked_list(l1,l2)
temp =  l3.head
while temp.next != None:
  print temp.value
  temp = temp.next
