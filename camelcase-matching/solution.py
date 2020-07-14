#https://leetcode.com/problems/camelcase-matching/submissions/


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        out = []
        for query in queries:
            if self.match(query, pattern):
                out.append(True)
            else:
                out.append(False)
        return out

    def match(self, query, pattern):
        next_index = -1
        for elem in pattern:
            prev_index = next_index
            next_index = query.find(elem, prev_index+1)
            print(next_index)
            if next_index == -1:
                return False
            else:
                if self.checkforCaps(query, prev_index+1, next_index-1):
                    return False
        if self.checkforCaps(query, next_index+1, len(query)-1):
                return False
        return True

    def checkforCaps(self, query, start, end):
        for i in range(start, end+1):
            if 65 <= ord(query[i])<= 90 :
                return True
        return False


