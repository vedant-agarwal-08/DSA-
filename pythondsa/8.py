# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
L=[1,10,25,30,50]
k=1
# k=500
# k=20
for i in range(0,len(L)):
    if(L[i]==k):
        print(i)      

if k not in L:
    L.append(k)
    L.sort()
    # print(L)
    for j in range(0,len(L)):
        if(k==L[j]):
            print(j)


n=int(input("number of element in a sorted list"))
L=[]
for i in range(0,n):
    e=int(input("enter element in sorted order"))
    L.append(e)
print(L)
k=int(input("enter element to be searched"))
for i in range(0,len(L)):
    if(k==L[i]):
        print(i)
if k not in L:
    L.append(k)
    L.sort()
    for j in range(0,len(L)):
        if(k==L[j]):
            print(j)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
   
  
  
  
   
   # for i in range(0,len(L)):
#     if(L[i]==k):
#         print(i)          
# for i in range(0,len(L)):
#     # print(i)
#     if(k>L[i] or k<L[i]):
#         print("")
# print(i)
# if (k>L[-1]):
#     print(len(L))
# if (k<L[0]):
#     print("0")
    
    