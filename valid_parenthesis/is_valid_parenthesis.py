class EmptyStack(Exception):
  def __init__(self, message):
    raise Exception(message)
class Stack:
	def __init__(self):
		self.top =  -1
		self.arr = []
		self.n = 0
	
	def push(self, elem):
		self.top += 1
		self.arr.append(elem)
		self.n += 1

	def pop(self):
		if self.n >0:
			elem =  self.top
			self.arr[self.top]  = None
			self.top -= 1
			self.n -= 1
		else:
			raise EmptyStack("Could not be deleted. emtpy Stack")



def is_valid_parenthesis(input_string):
  s =  Stack ()
  import pdb;pdb.set_trace()
  for elem in input_string:
  	try:
  		if elem == '(':
  			s.push('(')
  		else:
  			s.pop()
  	except Exception:
  		return False
  import pdb;pdb.set_trace()
  if s.n ==0:
  	return True
  else:
  	return False

#print is_valid_parenthesis("(())(")
print is_valid_parenthesis("(())()")
#print is_valid_parenthesis(")")  

