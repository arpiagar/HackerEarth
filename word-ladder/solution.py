#https://leetcode.com/problems/word-ladder/
class Solution(object):
    def diff(self, elem, subelem):
        out= []
        count = 0
        diff_char = ''
        for char in elem:
            if char not in subelem:
                count += 1
                diff_char = char
        if count == 1:
            return True

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        m1 = {}
        for elem in wordList:
            for subelem in wordList:
                if elem != subelem:
                    if self.diff(elem, subelem):
                        if m1.has_key(elem):
                            m1[elem].append(subelem)
                        else:
                            m1[elem] = [subelem]
        start = []
        for elem in wordList:
            if self.diff(beginWord, elem):
                start.append(elem)

