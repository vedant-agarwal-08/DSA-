# strs=["flower","flow","flight"]
strs=["dog","racecar","car"]
a=sorted(strs, key=len)
str1=""
b=[]
for i in range (0,len(a)):
    for j in range(0,len(a[i])):
        if(a[i][j]==a[i+1][j] and a[i][j]==a[i+2][j]):
            str1+=a[i][j]
            # b.append(a[i][j])
        if(str1==None):
            print (" ")
    # break
            
            # print(str1)
            # break
            # print(a[i][j])
            # print(str1)
    #     else:
    #         print("")
    print(str1)
            # print(b)
    
    break
    
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # strs=["flower","flow","flight"]
#         # strs=["dog","racecar","car"]
#         a=sorted(strs, key=len)
#         str1=""
        
#         for i in range (0,len(a)):
#             for j in range(0,len(a[i])-1):
#                 if(a[i][j]==a[i+1][j] and a[i][j]==a[i+2][j]):
#                     str1+=a[i][j]
#                 if(strs==None):
#                     return ""
            
            
#             # print(str1)
#             return str1
           
    
#             break