#bubble sort 
def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j]>my_list[j+1]:
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list
print(bubble_sort([2,3,6,5,4]))

#selection sort
def selection_sort(my_list1):
    for i in range(len(my_list1)-1):
        min_index=i
        for j in range(i+1,len(my_list1)):
            if my_list1[j]<my_list1[min_index]:
                min_index=j
        if i!=min_index:
            temp=my_list1[i]
            my_list1[i]=my_list1[min_index]
            my_list1[min_index]=temp
    return my_list1
print(selection_sort([2,3,6,5,4]))

#merge sort
def merge(list1,list2):
    combined=[]
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i<len(list1):
        combined.append(list1[i])
        i+=1
    while j<len(list2):
        combined.append(list2[j])
        j+=1

    return combined

def merge_sort(my_list):
    if len(my_list)==1:
        return my_list
    mid=int(len(my_list)/2)
    left=my_list[:mid]
    right=my_list[mid:]
    return merge(merge_sort(left),merge_sort(right))

print(merge_sort([2,3,6,5,4]))


def heapify(arr, n, i):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
  def heapSort(arr):
      n = len(arr)
  
      # Build max heap
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]
  
          # Heapify root element
          heapify(arr, i, 0)
  
  
  arr = [1, 12, 9, 5, 6, 10]
  heapSort(arr)
  n = len(arr)
  print("Sorted array is")
  for i in range(n):
      print("%d " % arr[i], end='')
  