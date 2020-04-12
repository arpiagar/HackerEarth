#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the commonChild function below.
def commonChild(s1, s2):
    print(s1,s2)
    if not len(s1) or not len(s2):
        return 0
    m = len(s1)
    n = len(s2)
    out = [[0] * m]* n
    if s2[0] == s1[0]:
        out[0][0] = 1
    for i in range(1,m):
        if s2[0] == s1[i]:
            out[0][i] = max(1,out[0][i-1]) 
        else:
            out[0][i] = out[0][i-1]
    for i in range(1,n):
        if s1[0] == s2[i]:
            out[i][0] == max(out[i-1][0] , 1)
        else:
            out[i][0] == out[i-1][0]

    for j in range(1, n):
        for i in range(1, m):      
            if s1[i] == s2[j]:
                out[j][i] = max(out[j-1][i-1]+1, out[j-1][i], out[j][i-1])
            else: 
                out[j][i] = max(out[j-1][i], out[j][i-1])
    return out[-1][-1]
if __name__ == '__main__':
