#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
    # Write your code here

def numberOfWays(n):
    hash_map = {0:0, 1:1, 2:1, 3:2}
    val = numberOfWaysOptimized(n, hash_map)
    return val

def numberOfWaysOptimized(n, hash_map):
    if n < 0:
        return -1
    if n in hash_map:
        return hash_map[n]
    value = numberOfWaysOptimized(n-1,hash_map) + numberOfWaysOptimized(n-3, hash_map)
    hash_map[n] = value % 1000000007
    return hash_map[n]

def test(n):
    hash_map = {0:0, 1:1, 2:1, 3:2}
    for i in range(0, n+1):
        val = numberOfWaysOptimized(i, hash_map)
    return val
if __name__ == '__main__':
    for i in range(0, 12):
        print(test(i))
