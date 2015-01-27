# 3456
# 3453
# 3553

# 345678

# 345673
# 345643
# 346643


# 346578
# 346573
# 346543
# 346643


def smallestGreaterPalindrome(number):
	n = len(number)
	if n % 2 == 0:
		for i in xrange(0,n%2-1):
			number[n-i] = number[i]
		number[n/2] = max(number[n/2],number[n/2-1])
		number[n/2-1] = number[n/2]
	return number 

n = int(raw_input())
for i in xrange(0,n):
	num = int(raw_input())
	print smallestGreaterPalindrome(num)