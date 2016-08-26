# Move zeros at the end of the array
def move_zeros(ip):
    zero_count = 0
    one_count = 0
    assignment_count = 0
    new_str = ""
    for elem in ip:
        if int(elem) == 0:
            zero_count += 1
        else:
            one_count += 1
        for i in xrange(0, one_count):
            if int(ip[i]) != 1:
                new_str[i] = "1"
                assignment_count += 1
                
        
        for i in xrange(one_count, len(ip)):
            if int(ip[i]) != 0:
                ip[i] = "0"
                assignment_count += 1
    return assignment_count

print move_zeros([1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,10])
print move_zeros([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
print move_zeros([0,0,0,0,0,1,1,1,1,1])