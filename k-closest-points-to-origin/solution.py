#https://leetcode.com/problems/k-closest-points-to-origin/submissions/


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def calc_distance(x:int, y:int) -> int:
            return x*x + y*y

        distance_map = {}
        for point in points:
                distance_map[tuple(point)] = calc_distance(point[0], point[1])
        sorted_list = sorted(distance_map.items(), key= lambda x: x[1])
        return [x[0] for x in sorted_list[0:K]]


