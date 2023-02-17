# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


L=[9,9]
s=""
c=[]
for i in range (0,len(L)):
    
    s=s+str(L[i])
print(s)
a=int(s)
num=str(a+1)
res = [int(x) for x in str(num)]
print(str(res))

# leetcode solution
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         # L=[1,2,3]
#         # L=[9,9]
#         s=""
#         c=[]
#         for i in range (0,len(digits)):
    
#             s=s+str(digits[i])
#         # print(s)
#         a=int(s)
#         num=str(a+1)
#         res = [int(x) for x in str(num)]
#         return res