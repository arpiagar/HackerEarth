class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_map = {}
        if len(words)<=1:
            return True
        for i,letter in enumerate(order):
            letter_map[letter] = i
        for i in range(1, len(words)):
            if not self.compareWords(words[i-1], words[i], letter_map):
                return False
        return True


    def compareWords(self, word1:str, word2:str, letter_map: hash) -> bool:
        min_length = min(len(word1), len(word2))
        for i in range(0, min_length):
            if letter_map[word1[i]] < letter_map[word2[i]]:
                return True
            elif letter_map[word1[i]] > letter_map[word2[i]]:
                return False
        if len(word1) > len(word2):
            return False
        return True
