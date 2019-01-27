class Solution(object):
    def longestCommonPrefix(self, strs):
        output = []
        len_array = [len(x) for x in strs]
        print len(strs)
        if not len(strs):
            return ""
        min_length = min(len_array)
        for i in xrange(0, min_length):
            character = strs[0][i]
            flag = True
            for string in strs[1:]:
                if string[i]  != character:
                    flag = False
            if flag:
                output.append(character)
            else:
                break
        return "".join(output)




        """
        :type strs: List[str]
        :rtype: str
        """

