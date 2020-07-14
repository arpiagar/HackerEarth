#https://leetcode.com/problems/hamming-distance/solution/

class Solution: # 011
                # 101
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:] #'1'
        bin_y = bin(y)[2:] #'100'
        count = 0
        if len(bin_x) < len(bin_y):
            min_b = len(bin_x)+1 # 2
            offset = len(bin_y) - len(bin_x) #2
        else:
            min_b = len(bin_y)+1
            offset = len(bin_x) - len(bin_y)
        for i in range(1,min_b):
            if bin_x[-i] != bin_y[-i]:
                count += 1 #1

        if len(bin_x) < len(bin_y):
            for i in range(0, offset):
                if bin_y[i] == '1':
                    count += 1
        else:
            print(bin_x[0:offset])
            for i in range(0, offset):
                if bin_x[i] == '1':
                    count += 1

        return count

