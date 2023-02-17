# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.



# s="   fly me   to   the moon  "
s="luffy is still joyboy"
count=0
a=s.split()
print(len(a[-1]))

for i in a[-1]:
    count+=1
print(count)

# leetcode code:-
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        a=s.split()
        # return len(a[-1])
        for i in a[-1]:
            count+=1
        return count
        