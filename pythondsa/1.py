# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# n=int(input())
nums=[2,7,9,11]
# for i in range(n):
#     e=int(input())
#     nums.append(e)
# print(nums)
output=[]
target=9
for i in range (0,len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i]+nums[j]==target:
            output.append(i)
            output.append(j)
print(output)

# main leetcode
# class Solution:
#     def twoSum(self,nums:List[int],target:int)->List[int]:
#         output=[]
#         for i in range (0,len(nums)):
#             for j in range (i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     output.append(i)
#                     output.append(j)
#         return output
            