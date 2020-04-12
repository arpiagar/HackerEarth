#https://leetcode.com/problems/insert-interval/submissions/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        current_index = -1
        out_list = []
        flag = True
        new_interval_start,new_interval_end = newInterval[0],newInterval[1]
        for i in range(0,len(intervals)) :
            interval = intervals[i]
            start, end = interval[0], interval[1]
            if new_interval_start < end and flag:
                if new_interval_start > start or new_interval_end > end:
                    current_index = i
                    if end == max(new_interval_end, end):
                        out_list.append(interval[i])
                        flag = False
                    else:
                        it1,it2,j = self.merge(intervals, i, new_interval_end )
                        out_list.append([it1,it2])
                        for k in range(j+1 , len(intervals)):
                            out_list.append(intervals[k])
                        return out_list
            else:
                out_list.append(intervals[i])
        return out_list

    def merge(self, intervals, index, interval_end):
        for i in range(index+1, len(intervals)):
            if interval_end >= intervals[i][0] and interval_end <= intervals[i][1] :
                return (intervals[index][0], max(interval_end,intervals[i][1]), i)
            elif interval_end <= intervals[i][0]:
                return (intervals[index][0], max(interval_end,intervals[index][1]), index)
        return intervals[index][0], interval_end, index
            #else:
            #    if interval_end <= intervals[i][1]:
            #        return (intervals[index][0], intervals[i][1], i)
