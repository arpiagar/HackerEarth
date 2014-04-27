import math

num = int(raw_input())

def isPrime(num):
	for i in xrange(2,int(math.sqrt(num)+1)):
		if num%i==0:
			return False
	return True
	
def whoWins(number):
	if  isPrime(number-2):
		print "Deepa"
		return
	else:
		for i in xrange(3,number,2):
			if isPrime(i) and isPrime(number-i):
				print "Deepa"
				return
	print  "Arjit"


for i in xrange(0,num):
	input=int(raw_input())
	whoWins(input)
