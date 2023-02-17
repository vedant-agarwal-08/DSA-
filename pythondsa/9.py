# happy number
# 1
n=int(input())
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
    x=sum
if(x==1):
    print("happy number")
else:
    print("not a happy number")

# 2 not working 
n=input("enter number")
def sum():
    sum1=0
    L=[]
    for i in n:
        L.append(int(i))
    # print(L)
    for j in L:
        sum1=sum1+j**2
    print(sum1)
    
    while (sum1>=9):
        sum()
        if (sum1==1):
            return("happy number") 
        else:
            return ("not happy number")
sum()
    