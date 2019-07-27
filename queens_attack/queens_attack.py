#!/bin/python

import math
import os
import random
import re
import sys


def process_row(n,r_q,c_q, obstacles_map):
    count = 0
    j = c_q-1
    while (j > 0):
        if obstacles_map.has_key((r_q,j)):
            break
        else:
            count +=1
            j -= 1
    j = c_q+1
    while (j <= n):
        if obstacles_map.has_key((r_q,j)):
            break
        else:
            count +=1
            j += 1

    return count

def process_col(n,r_q,c_q, obstacles_map):
    count = 0
    i = r_q-1
    while (i > 0):
        if obstacles_map.has_key((i,c_q)):
            break
        else:
            count +=1
            i -= 1
    i = r_q +1
    while (i <= n ):
        if obstacles_map.has_key((i,c_q)):
            break
        else:
            count +=1
            i += 1
    return count

def process_diagonal(n, r_q, c_q, obstacles_map):
    count  = 0
    i = r_q - 1
    j = c_q - 1
    #bottom left
    while(i >0 and j > 0):
        if obstacles_map.has_key((i,j)):
            break
        else:
            count += 1
            i -= 1
            j -= 1
    i = r_q + 1
    j = c_q + 1
    #top right
    while (i <= n and j <= n):
        if obstacles_map.has_key((i,j)):
            break
        else:
            count += 1
            i += 1
            j += 1
    i = r_q + 1
    j = c_q - 1
    #top left
    while (i <=n and j > 0 ):
        if obstacles_map.has_key((i,j)):
            break
        else:
            count += 1
            i += 1
            j -= 1
    i = r_q - 1
    j = c_q + 1
    #bottom right
    while (i >0 and j <= n):
        if obstacles_map.has_key((i,j)):
            break
        else:
            count += 1
            i -= 1
            j += 1
    return count




# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles_map = {}
    for elem in obstacles:
        row,col = elem[0],elem[1]
        obstacles_map[(row,col)] =  1

    return process_col(n, r_q, c_q, obstacles_map) + process_diagonal(n, r_q, c_q, obstacles_map) + process_row(n, r_q, c_q, obstacles_map)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = raw_input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in xrange(k):
        obstacles.append(map(int, raw_input().rstrip().split()))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

