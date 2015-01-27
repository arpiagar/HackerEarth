def reverse(ip_str):
	i = 0
	j = len(ip_str)-1
	while i<j:
		temp = ip_str[i]
		ip_str[i] = ip_str[j]
		ip_str[j] = temp
		i += 1
		j -= 1
	return ip_str

#I am a developer
#repoleved a ma I
#developer a am I

def reverse_words(ip_str):
	i = 0
	temp = []
	while(i < len(ip_str)):
		if ip_str[i] != " ":
			temp.append(ip_str[i])
		else:
			#import pdb;pdb.set_trace()
			k = reverse(temp)
			ip_str[i-len(temp):i] = k[0:len(k)]
			temp = []
		i += 1
	return ip_str

if __name__ == "__main__":
	input1 =  raw_input()
	input1 =  [x for x in input1]
	input1 = reverse(input1)
	input1 = reverse_words(input1)
	print "".join(input1)

