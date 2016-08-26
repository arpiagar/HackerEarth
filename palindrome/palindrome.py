

s = "A man, a plan, a canal, Panama!"

def fu(s):
    limit1 = (97,122)
    limit2 = (65,90)

    n = len(s)

    i = 0
    j = n-1

    while (i<j):
        while not ((ord(s[i]) >=97 and ord(s[i]) <=122) or (ord(s[i]) >=65 and ord(s[i]) <=90)):
            i += 1
        while not ((ord(s[j]) >=97 and ord(s[j]) <=122) or (ord(s[j]) >=65 and ord(s[j]) <=90)):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

print fu(s)