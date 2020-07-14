class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        out = []
        found_set = set([])
        for i in range(len(A)):
            x1,y1 = A[i] # 13,23
            for j in range(len(B)):
                x2,y2 = B[j] # [15,24]
                if x2 > y1:
                    break
                if x2<= x1 <= y2:
                    if (x1,min(y1,y2)) not in found_set:
                        found_set.add((x1,min(y1,y2)))
                        out.append((x1,min(y1,y2))) # (1,2), (5,5), (8,10), (15,23),
                if x2<= y1 <=y2:
                    if (max(x1,x2), y1) not in found_set:
                        found_set.add((max(x1,x2), y1))
                        out.append((max(x1,x2), y1)) #(1,2)
                if x1< x2 < y1 and x1< y2 < y1:
                    if (x2, y2) not in found_set:
                        found_set.add((x2, y2))
                        out.append((x2, y2)) #(1,2)
                
        return out
                
