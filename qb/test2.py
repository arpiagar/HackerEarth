#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedOrNot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY expressions
#  2. INTEGER_ARRAY maxReplacements
#

def balancedOrNot(expressions, maxReplacements):
    # Write your code here
    out_array = []
    for i in range(0, len(expressions)):
        diff, open_count = find_diff_in_expression(expressions[i])
        import pdb;pdb.set_trace()
        if open_count > 0:
            out_array.append(0)
        else:
            if diff < 0:
                out_array.append(0)
            else:
                if diff <= maxReplacements[i]:
                    out_array.append(1)
                else:
                    out_array.append(0)
    return out_array
def find_diff_in_expression(exp):
    less_than_count = greater_than_count = 0
    open_count = 0
    import pdb;pdb.set_trace()
    for symbol in exp:
        if symbol == "<":
            open_count += 1
            less_than_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            greater_than_count += 1
    return (greater_than_count - less_than_count), open_count

if __name__ == '__main__':
    experessions = ["<>><"]
    maxReplacements = [1]
    print(balancedOrNot(experessions, maxReplacements))
