#
# Function which array of chars and do word wise reverse, in-place
# input : "This is a test", is modified to "test a is This"
# 
# tset a si siht
# test a is 
# ['T', 'h', 'i', 's',...'] 
# 

def rev(start,end,input_string):
    n = (end-start+1)/2
    for i in xrange(0,n):
        temp = input_string[start+i]
        input_string[start+i] = input_string[end-i]
        input_string[end-i] = temp
    

def reverse(input_string):
    n = len(input_string)
    input_string = [x for x in input_string]
    rev(0,len(input_string)-1,input_string)

    count = 0
    i = 0
    start = 0
    while count < n:
        if input_string[start+i] != " ":
            i += 1
        else:
            rev(start,start+i-1, input_string)
            i = 0
            start = count+1
        count += 1
    rev(start,start+i-1, input_string)
    return input_string
    
    
if __name__ == "__main__":
    print reverse([x for x in "This is a test"])
    print reverse([x for x in "Are you sure?"])
    

  