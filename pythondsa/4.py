s="MCMXCIV"
sum=0
for i in s:
    if i=="I":
        sum=sum+1
    elif i=="V":
        sum=sum+5
    elif i=="X":
        sum=sum+10
    elif i=="L":
        sum=sum+50
    elif i=="C":
        sum=sum+100
    elif i=="D":
        sum=sum+500
    elif i=="M":
        sum=sum+1000
print(sum)
# s="MCMXCIV"
# sum=0
# a=[]
# for j in s:
#     a.append(j)
# print(a)
# for i in range(0,len(a)):
#     if i=="I":
#         sum=sum+1
        
#     elif i=="V":
#         sum=sum+5
        
#     elif i=="X":
#         sum=sum+10
        
#     elif i=="L":
#         sum=sum+50
        
#     elif i=="C":
#         sum=sum+100
        
#     elif i=="D":
#         sum=sum+500
        
#     elif i=="M":
#         sum=sum+1000
#     elif (a[i]=="I" and a[i+1]=="V"):
#         sum=sum+4
#     elif(a[i]=="I" and a[i+1]=="X"):
#         sum+=9
#     elif(a[i]=="C" and a[i+1]=="D"):
#         sum+=400
#     elif(a[i]=="C" and a[i+1]=="M"):
#         sum+=900
    
# print(sum)
        
    