#https://leetcode.com/problems/interval-list-intersections/submissions/


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        first_index = second_index = 0
        out = []
        first_list_length = len(A)
        second_list_length = len(B)
        while(first_index < first_list_length and second_index < second_list_length):
            min1,max1 = A[first_index]
            min2,max2 = B[second_index]
            if min1 > max2:
                second_index += 1
            elif min2 > max1:
                first_index += 1
            elif min2 <= min1 <= max2:
                if max1 > max2:
                    out.append([min1, max2])
                    second_index += 1
                elif max2 > max1:
                    out.append([min1, max1])
                    first_index += 1
                else:
                    out.append([min1, max2])
                    first_index += 1
                    second_index += 1
            elif min1 <= min2 <= max1:
                if max1 > max2:
                    out.append([min2, max2])
                    second_index += 1
                elif max2 > max1:
                    out.append([min2, max1])
                    first_index += 1
                else:
                    out.append([min2, max2])
                    first_index += 1
                    second_index += 1
        return out
