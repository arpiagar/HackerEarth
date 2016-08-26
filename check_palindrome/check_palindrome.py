
#Check Palindrome - all variations
def check_palindrome(ip):
    n = len(ip)
    i = 0
    j = len(ip) -1 
    while i<j:
        if ip[i] != ip[j]:
            return False
        i += 1
        j -= 1
    
    return True

print check_palindrome("")
print check_palindrome("a")
print check_palindrome("aa")
print check_palindrome("aba")
print check_palindrome("abba")
print check_palindrome("abbab")
