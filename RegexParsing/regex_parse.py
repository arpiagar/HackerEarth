# Write a function to check if a string matches a regex patter. Note that you only have to deal with patterns containing "*". Also, note that the pattern can't start with "*". 

# Some examples: 
# isMatch(“aa”,”a”) → false 
# isMatch(“aa”,”aa”) → true 
# isMatch(“aaa”,”aa”) → false 
# isMatch(“aa”, “a*”) → true 
# isMatch(“aa”, “*”) → true 
# isMatch(“ab”, “*”) → true 
# isMatch(“ab”, “*”) → true 
# isMatch(“b*a”, “a”) → true 
# isMatch(“a*a”, “a”) → true 
# isMatch(“aab”, “c*a*b”) → true

def is_match(string,regex):
    if regex == '*':
        return True
    return is_match_index(string,regex,0,0)

def is_match_index(string, regex, index, r_index):
    is_string_end =  False
    is_regex_end = False
    
    if index >= len(string)-1:
        is_string_end = True
    if r_index >=  len(regex)-1:
        is_regex_end =  True 
    
    if  is_string_end and is_regex_end:
        return True
    if not is_string_end and is_regex_end:
        return False
    
    alphabet =  regex[r_index]
    if r_index+1 < len(regex):
        next_alphabet = regex[r_index+1]
   
    if next_alphabet == "*" and index < len(string):
        return is_match_index(string,regex,index,r_index+2) or is_match_index(string,regex,index+1,r_index)
    else:
        if is_string_end:
            return False
        string_alphabet  =  string[index]
        if alphabet == string_alphabet:
            return is_match_index(string,regex,index+1,r_index+2)
        else:
            return False
    
    
if __name__ == "__main__":
    print is_match("aabc","a*b*c")
    print is_match("aabbc","a*b*bc")
    print is_match("bbc","a*b*bc")
    print is_match("ac","a*b*bc")
        
    
    
            
            
            
   