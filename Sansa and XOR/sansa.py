n = int(raw_input())

def XORResult(num_list,n):
    maj_xor =  None
    for size in range(1,n+1):
        for i in range(0,n-size+1):
            min_xor = None
            for j in range(0,size):
                if min_xor ==  None:
                    min_xor =  num_list[i+j]
                else:
                    min_xor ^= num_list[i+j]
            if maj_xor == None:
                maj_xor =  min_xor
            else:
                maj_xor ^= min_xor
            
    return maj_xor

for i in range(0,n):
    num =  int(raw_input())
    num_list = raw_input().split(" ")
    num_list = [int(x) for x in num_list]
    print XORResult(num_list,num)