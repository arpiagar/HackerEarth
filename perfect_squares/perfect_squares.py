class Solution(object):
    def numSquares(self, n):
        s_map = {}
        min_count = self.calculate_min_num(n, s_map, 0)
        return min_count
        """
        :type n: int
        :rtype: int
        """
    def calculate_min_num(self,n, s_map, count):
        print "Hello",n,count,s_map
        #if s_map.has_key(n):
        #    return count+s_map[n]
        max_sqrt = int(math.floor(math.sqrt(n)))
        temp_count = n
        for i in xrange(max_sqrt, 0, -1):
            if n-i*i == 0:
                s_map[n] = 1
                print n,i,count
                return count+1
            else:
                print "Temp Before",n,temp_count,i,count
                if s_map.has_key(n):
                    temp_count = min(temp_count, s_map[n])
                else:
                    temp_count = min(temp_count, self.calculate_min_num(n-i*i, s_map, count+1))
        print "Temp After",n,temp_count

        #s_map[n] = temp_count
        return count+temp_count
