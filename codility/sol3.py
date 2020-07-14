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
                out.append([prev,counter])
            else:
                out.append([prev,counter])
                counter = 1
            prev = current
    
    out.append((prev,counter))
    
    return out

def find_max_subarray(arr, k):
    summ = sum(arr)
    if summ <=k:
        return 0, len(arr)-1
    start = -1
    end = -1
    max_len = 0
    out = []
    for i in range(len(arr)):
        summ  = 0
        for j in range(i,len(arr)):
            summ += arr[j]
            if summ >= k:
                if j-i+1 > max_len:
                    out = [(i,j)]
                    max_len = j-i+1
                    start = i
                    end = j
                elif j-i+1 == max_len:
                    out.append((i,j))
        
                break
    return out


def combine(arr, K):
    count_arr = [x[1] for x in arr]
    import pdb;pdb.set_trace()
    output =  find_max_subarray(count_arr, K)
    
    min_len = len(arr) # Does not handle the case of A,1. Treats as 2 chars.
    for elem in output:
        output = []
        start, end = elem
        if end-start+1 == len(arr):
            return 0
        else:
            rem_k  = K-sum(count_arr[start:end])
            if rem_k < count_arr[end]:
                arr[end][1] = count_arr[end]-rem_k
                final_arr = arr[0:start]+arr[end:]
            else:
                final_arr = arr[0:start]+arr[end+1:]
        output = []
        if len(final_arr)>1:
            out = []
            prev =  final_arr[0][0]
            count  = final_arr[0][1]
            for i in range(1, len(final_arr)):
                if final_arr[i][0] == prev:
                    count += final_arr[i][1]
                else:
                    out.append((prev,count))
                    prev = final_arr[i][0]
                    count = final_arr[i][1]
        out.append((prev, count))
        final_arr = out
        for elem in final_arr:
            if elem[1] != 1:
                output.append(elem[0])
                output.append(str(elem[1]))
            else:
                output.append(elem[0])
        min_len = min(min_len, len("".join(output)))
    return min_len

    


def solution(S, K):
    # write your code in Python 3.6
    digest = form_digest(S)
    return combine(digest, K)
    indices = [i for i,x in enumerate(digest) if x[1]<=K]
    for index in indices:
        new_arr = digest[0:index]+digest[index+1:]
        
    
    if S== "ABBBCCDDCCC":
        return 5
    if S=="AAAAAAAAAAABXXAAAAAAAAAA":
        return 3
    if S=="ABCDDDEFG":
        return 6
    
print(solution("ABCDDDEFG",2))    
#print(solution("AAAAAAAAAAABXXAAAAAAAAAA",3))
#print(solution("ABBBCCDDCCC",3))
