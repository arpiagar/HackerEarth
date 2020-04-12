# Link: https://leetcode.com/problems/decode-ways
class Solution(object):
    def countRecurse(self, index, input_s, current_list, out_list, n, wordmap):
        if index >= n:
            return
        elif index == n-1:
            if input_s[index] != "0":
                current_list.append(input_s[index])
                out_list.append(current_list)
            return
        else:
            temp_list = [x for x in current_list]
            if input_s[index] != "0":
                current_list.append(input_s[index])
                self.countRecurse(index+1, input_s, current_list, out_list, n, wordmap)
            elem = int(input_s[index:index+2])
            if elem < 27 and elem > 9:
                temp_list.append(wordmap[elem])
                if index == n-2 :
                    out_list.append(temp_list)
                else:
                    self.countRecurse(index+2,input_s,temp_list,out_list,n,wordmap)
            return

    def numDecodings(self, s):
        wordmap = {}
        for i in xrange(1,27):
            wordmap[i] = chr(96+i)

        n = len(s)
        out_list = []
        if n == 0:
            return 0
        self.countRecurse(0, s, [], out_list, n, wordmap)
        out_list = ["".join(x) for x in out_list]
        return len(list(set(out_list)))


        """              6
        :type s: str
        :rtype: int
        """

