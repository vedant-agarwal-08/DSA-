#Creating array
import array as array
a=array.array('i',[1,2,3,4,5])
print(a)

# Accessing array elements
print(a[0])
print(a[-1])

#Appending element
a.append(6)
print(a)

#Inserting an element
a.insert(2,7)
print(a)

#extending an array
a.extend([8,9,10])
print(a)

#Removing an element
a.remove(10)
print(a)

#removing element from a specific position
del a[2]
print(a,"..")

#search an index of element
print(a.index(5))

#updation 
a[1]=0
print(a)

#traversing
for i in a:
    print(i)