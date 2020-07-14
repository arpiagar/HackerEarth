#https://leetcode.com/problems/string-compression/submissions/

class Solution:
    def compress(self, chars: List[str]) -> int: #["a","a","b","b","c","c","c","d"]
        if not chars or len(chars)==1:
            return len(chars)
        counter = 1
        new_counter = 0
        char_count = 1
        prev_char = chars[0]
        while(counter < len(chars)):
            current_char = chars[counter]
            if current_char == prev_char:
                char_count += 1
            else:
                if char_count == 1:
                    chars[new_counter] = prev_char
                    new_counter += 1

                else:
                    chars[new_counter] = prev_char
                    new_counter += 1
                    for elem in str(char_count):
                        chars[new_counter] = elem
                        new_counter += 1
                    char_count = 1
                prev_char = current_char
            counter += 1

        chars[new_counter] = prev_char
        if char_count > 1:
            new_counter+=1
            for elem in str(char_count):
                chars[new_counter] = elem
                new_counter += 1
            return new_counter
        return new_counter+1



