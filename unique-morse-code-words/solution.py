i#https://leetcode.com/problems/unique-morse-code-words/submissions/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_map = {}
        for i in range(0, 26):
            morse_map[chr(ord('a')+i)] = morse[i]
        word_map = {}
        for word in words:
            word_map[self.generate(word, morse_map)] = 1
        return len(word_map.keys())


    def generate(self, word, morse_map):
        out = ""
        for letter in word:
            out += morse_map[letter]
        return out
