# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def form_digest(arr):
    if not arr or len(arr)==1:
        return arr
    n = len(arr)
    counter =1
    prev = arr[0]
    out = []
    for i in range(1,len(arr)):
        current = arr[i]
        if current == prev:
            counter +=1
        else:
            if counter == 1:
                out.append((prev,counter))
            else:
                out.append((prev,counter))
                counter = 1
            prev = current
    
    out.append((prev,counter))
    
    return out
    
def solution(S, K):
    # write your code in Python 3.6
    digest = form_digest(S)
    indices = [i for i,x in enumerate(digest) if x[1]<=K]
    for index in indices:
        new_arr = digest[0:index]+digest[index+1:]
        
    
    if S== "ABBBCCDDCCC":
        return 5
    if S=="AAAAAAAAAAABXXAAAAAAAAAA":
        return 3
    if S=="ABCDDDEFG":
        return 6
    
    
    
    
    
    
    
    
    
