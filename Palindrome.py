# -*- coding:utf-8 -*-
# creating a palindrome(回数)

def _is_palindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] == s[-i-1]:
            pass
        else:
            return False
    return True

output = filter(_is_palindrome, range(1, 10000))
print(list(output))