#https://leetcode.com/problems/online-stock-span/solution/

class StockSpanner:

    def __init__(self):
        self.span_list = []
        self.counter_list = []
        self.top = None


    def next(self, price: int) -> int:
        if self.top == None: # [100],[80],[60],[70],[60],[75],[85]
            ret_val = 1
        else:
            if price < self.top:
                ret_val = 1
            else:
                counter = len(self.span_list)-1 #2
                count = 1
                while (counter >=0 and self.span_list[counter] <= price):
                    count += self.counter_list[counter]
                    counter -= self.counter_list[counter]
                ret_val = count
        self.top = price # 60
        self.span_list.append(price) # [100,80, 60,70,60,75]
        self.counter_list.append(ret_val)
        return ret_val

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
