import math
def numberOfWays1(n):
    count = n//3
    num_ways = 0
    for i in range(0, count+1):
        count_of_threes = i
        count_of_ones = n - count_of_threes * 3
        num_ways += ncr((count_of_ones+count_of_threes), count_of_threes)
    return num_ways % 1000000007
    # Write your code here

def ncr(n,r):
    f = math.factorial
    return f(n)//(f(r)*f(n-r))




def numberOfWays(n):
    hash_map = {}
    val = numberOfWaysOptimized(n, hash_map)
    #print(val)

    return val
def numberOfWaysOptimized(n, hash_map):
    if n in hash_map:
        return hash_map[n]
    if n == 0 :
        return 0
    if n == 1 or  n == 2:
        return 1
    if n == 3:
        return 2
    value = numberOfWaysOptimized(n-1, hash_map) + numberOfWaysOptimized(n-3, hash_map)
    hash_map[n] = value
    return value

import functools
@functools.lru_cache(None)
def numberOfWays2(n):
    if n == 0 :
        return 0
    if n == 1 or  n == 2:
        return 1
    if n == 3:
        return 2
    value = numberOfWays(n-1) + numberOfWays(n-3)
    return value

if __name__ == "__main__":
    for i in range(1, 11):
        print(numberOfWays2(i))
    #print(numberOfWays(7))
    #print(numberOfWays(1))
    #print(numberOfWays(9))
