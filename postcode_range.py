start = "AB123Z"
end = "AC999B"

def increment_character(character, carry):

    if carry+ord(character) < ord("Z"):
        new_character = chr(ord(character)+1)
        carry = 0
    else:
        carry = 1
        new_character = "A"
    return new_character,carry

def increment_num(num, carry):
    if ord(num)+carry < 1+ord("9"):
        new_num = chr(ord(num) +1)
        carry = 0
    else:
        carry = 1
        new_num = "0"
    return new_num, carry

def increment_word(word, carry):
    idx = len(word)-1

    elem =  word[idx]
    if carry+ord(elem) <= ord("9")+1:
        new_digit, carry = increment_num(elem, carry)
    else:
        new_digit, carry =  increment_character(elem, carry)
    word = word[0:idx]+new_digit+word[idx+1:len(word)]
    if carry == 1:
        idx -= 1
    while(idx >=0 and carry == 1):
        elem =  word[idx]
        if carry+ord(elem) <= 1+ord("9"):
            new_digit, carry = increment_num(elem, carry)
        else:
            new_digit, carry =  increment_character(elem, carry)

        word = word[0:idx] + new_digit + word[idx+1:len(word)]
        if carry == 1:
            idx -= 1
    if idx == -1:
        if ord(word[idx+1]) < ord("9"):
            return '1'+word
        else:
            return "A"+word
    return word


carry = 0
out_list = []
while (start != end):
    start =  increment_word(start, 0)
    print start
    out_list.append(start)




