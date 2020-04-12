##https://leetcode.com/problems/longest-common-subsequence/submissions/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        perf_map = {}

        return self.longestCommonSubsequencePerf(text1, text2, perf_map)

    def longestCommonSubsequencePerf(self, text1, text2, perf_map):
        if (text1,text2) in perf_map:
            return perf_map[(text1,text2)]
        if not len(text1) or not len(text2):
            return 0
        else:
            a1 = text1[0]
            a2 = text2[0]
            if a1 == a2:
                perf_map[(text1,text2)] = 1 + self.longestCommonSubsequencePerf(text1[1:], text2[1:],perf_map)
                return perf_map[(text1,text2)]
            else:
                perf_map[(text1,text2)] = max(self.longestCommonSubsequencePerf(text1,text2[1:],perf_map),self.longestCommonSubsequencePerf(text1[1:],text2,perf_map))
                return perf_map[(text1,text2)]
