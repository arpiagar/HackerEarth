#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/


from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_map = defaultdict(int)
        length = 0
        for char in chars:
            freq_map[char] += 1
        for word in words:
            if self.can_be_constructed(word, freq_map):
                length += len(word)
        return length


    def can_be_constructed(self, word, freq_map):
        word_map = freq_map.copy()
        for char in word :
            if char not in word_map:
                return False
            if not word_map[char]:
                return False
            word_map[char] -= 1
        return True
