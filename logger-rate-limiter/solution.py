i#https://leetcode.com/problems/logger-rate-limiter/submissions/



class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linked_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.linked_map:
            t = self.linked_map[message]
            if timestamp - t < 10:
                return False
            else:
                self.linked_map.pop(message)
                self.linked_map[message] = timestamp
                return True
        else:
            if len(self.linked_map.keys()) == 10:

                v = list(self.linked_map.keys())[0]
                self.linked_map.pop(v)
            self.linked_map[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
