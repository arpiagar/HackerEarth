
class Solution(object):
    def findAllIndices(self, s,character):
        ret_list = []
        for i in xrange(0, len(s)):
            elem = s[i]
            if elem == character:
                ret_list.append(i)
        return ret_list

    def isMatch(self, s, p):
        if len(p):
            if p[0] == "?":
                if len(s):
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
            elif p[0] == "*":
                if len(p) == 1:
                    return True
                else:
                    if p[1] == "*":
                        return self.isMatch(s, p[1:])
                    elif p[1] == "?":
                        if len(p) == 2:
                            if len(s):
                                return True
                            else:
                                return False
                        else:
                            if len(s):
                                return self.isMatch(s[1:], p[2:])
                            else:
                                return False
                    else:
                        character = p[1]
                        idx_list = self.findAllIndices(s,character)
                        flag = False
                    for idx in idx_list:
                        flag = flag or self.isMatch(s[idx+1:],p[2:])
                    return flag
            else:
                if len(s):
                    if p[0] != s[0]:
                        return False
                    else:
                        return self.isMatch(s[1:],p[1:])
                else:
                    return False
        else:
            if len(s):
                return False
            else:
                return True




        """
        :type s: str
        :type p: str
        :rtype: bool
        """

