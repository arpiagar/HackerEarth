import heapq


class Solution:
    def dist(self, point):
        return point[0]*point[0] + point[1]*point[1]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return 
        arr = []
        heapmap = {}
        count = 0
        max_dist = self.dist(points[0])
        for elem in points:
            dist =self.dist(elem)
            if count < K:
                if dist not in heapmap:
                    heapmap[dist] = [elem]
                else:
                    heapmap[dist].append(elem)
                max_dist = max(max_dist, max(heapmap.keys()))
                count += 1
            else:
                if dist < max_dist:
                    
                    if len(heapmap[max_dist]) == 1:
                        heapmap.pop(max_dist)
                    else:
                        heapmap[max_dist].pop()
                    if dist not in heapmap:
                        heapmap[dist] = [elem]
                    else:
                        heapmap[dist].append(elem)
                    max_dist = max(heapmap.keys())
        out = []
        for x in heapmap.values():
            out = out +x
        return out
        
                    
    
