#https://leetcode.com/problems/moving-average-from-data-stream/submissions/


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.l = []
        self.curr_sum = 0
        self.count = 0



    def next(self, val: int) -> float:
        if self.count < self.size:
            self.count += 1
            self.curr_sum += val
            self.l.append(val)
            return float(self.curr_sum/self.count)
        else:
            first = self.l.pop(0)
            self.l.append(val)
            self.curr_sum += val
            self.curr_sum -= first
            return float(self.curr_sum/self.count)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
