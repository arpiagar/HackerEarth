#https://www.geeksforgeeks.org/longest-consecutive-subsequence/

def consecutive_subsequence(self, arr):
    s = set([])
    ans = 0
    for elem in arr:
        s.add(elem)
    for i in range(len(arr)):
        #Check whether it's not the second or third etc element in the set.
        if arr[i-1] in s:
            j = arr[i]
            while j in s:
                j += 1
            ans = max(ans, j-arr[i])
    return ans

        
