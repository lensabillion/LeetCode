s = list(input().split())
# print(s)
# def palindrome(s):
#     i = 0
#     j = len(s) - 1
#     while i < j:
#         if s[i] != s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
# print(palindrome(s)) 
def recur_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return recur_palindrome(s[1:len(s)-1] )
    
    return False
    
print(recur_palindrome(s))