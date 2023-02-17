# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
def reverse():
    n=int(input())
    s=str(n)
    rev=""
    for i in s:
        rev=i+rev
    # b=rev
    if rev==s:
        return True
    else:
        return False
reverse()


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # x=int(input())
#         s=str(x)
#         rev=""
#         for i in s:
#             rev=i+rev
#         print(rev)
#         # print(rev)
#         if(rev==s):
#             return True
#         else:
#             return False
    
        
