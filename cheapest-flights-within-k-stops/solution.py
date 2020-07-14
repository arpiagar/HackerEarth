#https://leetcode.com/problems/cheapest-flights-within-k-stops/

import sys
import copy
class Solution:
    def find_min(self, src, dest, k, visited_map, arr,memoized):
        if src == dest:
            return 0
        if k < 0:
            return sys.maxsize
        if (src,k) in self.memoized:
            return self.memoized[(src,k)]
        min_val = sys.maxsize
        for i in range(len(arr)):
            if i not in visited_map and arr[src][i]!=0 and i!=src:
                new_map = copy.deepcopy(visited_map)
                new_map[src] = 1
                if i == dest:
                    min_val = min(min_val, arr[src][i])
                min_val = min(min_val, arr[src][i]+ self.find_min(i, dest, k-1,new_map,arr, memoized ))
        self.memoized[(src,k)] = min_val
        return min_val

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        arr = [[0 for i in range(n)] for i in range(n)]
        memoized = [[sys.maxsize for i in range(n+1)] for i in range(n+1)]
        self.memoized = {}
        for elem in flights:
            source, dest, weight = elem
            arr[source][dest] = weight
        visited_map = {}
        v= self.find_min(src, dst, K, visited_map, arr, memoized)
        print(v, sys.maxsize)
        if v >= sys.maxsize:
            return -1
        return v


